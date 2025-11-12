from flask import Blueprint, request, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from .models import *
from . import db
from datetime import datetime
import secrets
from sqlalchemy import or_

api = Blueprint('api', __name__)

# Authentication APIs
@api.route('/api/auth/register', methods=['POST'])
def register():
    data = request.get_json()
    
    if Customer.query.filter_by(email=data['email']).first():
        return jsonify({'error': 'Email already exists'}), 400
    
    if Customer.query.filter_by(username=data['username']).first():
        return jsonify({'error': 'Username already exists'}), 400
    
    customer = Customer(
        email=data['email'],
        username=data['username'],
        first_name=data.get('first_name'),
        last_name=data.get('last_name'),
        phone=data.get('phone')
    )
    customer.password = data['password']
    
    db.session.add(customer)
    db.session.commit()
    
    return jsonify({'message': 'User created successfully', 'user': customer.to_dict()}), 201

@api.route('/api/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    customer = Customer.query.filter_by(email=data['email']).first()
    
    if customer and customer.verify_password(data['password']):
        login_user(customer)
        customer.last_login = datetime.utcnow()
        db.session.commit()
        return jsonify({'message': 'Login successful', 'user': customer.to_dict()}), 200
    
    return jsonify({'error': 'Invalid credentials'}), 401

@api.route('/api/auth/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'Logged out successfully'}), 200

@api.route('/api/auth/profile', methods=['GET'])
@login_required
def get_profile():
    return jsonify(current_user.to_dict()), 200

@api.route('/api/auth/profile', methods=['PUT'])
@login_required
def update_profile():
    data = request.get_json()
    
    for field in ['first_name', 'last_name', 'phone']:
        if field in data:
            setattr(current_user, field, data[field])
    
    db.session.commit()
    return jsonify(current_user.to_dict()), 200

# Category APIs
@api.route('/api/categories', methods=['GET'])
def get_categories():
    categories = Category.query.filter_by(is_active=True).all()
    return jsonify([cat.to_dict() for cat in categories]), 200

@api.route('/api/categories', methods=['POST'])
@login_required
def create_category():
    if not current_user.is_admin:
        return jsonify({'error': 'Admin access required'}), 403
    
    data = request.get_json()
    category = Category(
        name=data['name'],
        description=data.get('description'),
        image=data.get('image')
    )
    
    db.session.add(category)
    db.session.commit()
    
    return jsonify(category.to_dict()), 201

@api.route('/api/categories/<int:category_id>', methods=['PUT'])
@login_required
def update_category(category_id):
    if not current_user.is_admin:
        return jsonify({'error': 'Admin access required'}), 403
    
    category = Category.query.get_or_404(category_id)
    data = request.get_json()
    
    for field in ['name', 'description', 'image', 'is_active']:
        if field in data:
            setattr(category, field, data[field])
    
    db.session.commit()
    return jsonify(category.to_dict()), 200

# Product APIs
@api.route('/api/products', methods=['GET'])
def get_products():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 20, type=int)
    category_id = request.args.get('category_id', type=int)
    search = request.args.get('search', '')
    featured = request.args.get('featured', type=bool)
    
    query = Product.query.filter_by(is_active=True)
    
    if category_id:
        query = query.filter_by(category_id=category_id)
    
    if search:
        query = query.filter(or_(
            Product.product_name.contains(search),
            Product.description.contains(search)
        ))
    
    if featured:
        query = query.filter_by(is_featured=True)
    
    products = query.paginate(page=page, per_page=per_page, error_out=False)
    
    return jsonify({
        'products': [product.to_dict() for product in products.items],
        'total': products.total,
        'pages': products.pages,
        'current_page': page
    }), 200

@api.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = Product.query.get_or_404(product_id)
    return jsonify(product.to_dict()), 200

@api.route('/api/products', methods=['POST'])
@login_required
def create_product():
    if not current_user.is_admin:
        return jsonify({'error': 'Admin access required'}), 403
    
    data = request.get_json()
    
    product = Product(
        product_name=data['product_name'],
        description=data.get('description'),
        product_quantity=data['product_quantity'],
        price=data['price'],
        old_price=data.get('old_price'),
        vendor=data['vendor'],
        product_img=data.get('product_img'),
        sku=data.get('sku'),
        weight=data.get('weight'),
        dimensions=data.get('dimensions'),
        category_id=data.get('category_id'),
        is_featured=data.get('is_featured', False),
        flash_sale=data.get('flash_sale', False),
        discount_percentage=data.get('discount_percentage', 0)
    )
    
    db.session.add(product)
    db.session.commit()
    
    return jsonify(product.to_dict()), 201

@api.route('/api/products/<int:product_id>', methods=['PUT'])
@login_required
def update_product(product_id):
    if not current_user.is_admin:
        return jsonify({'error': 'Admin access required'}), 403
    
    product = Product.query.get_or_404(product_id)
    data = request.get_json()
    
    for field in ['product_name', 'description', 'product_quantity', 'price', 'old_price', 
                  'vendor', 'product_img', 'sku', 'weight', 'dimensions', 'category_id',
                  'is_active', 'is_featured', 'flash_sale', 'discount_percentage']:
        if field in data:
            setattr(product, field, data[field])
    
    db.session.commit()
    return jsonify(product.to_dict()), 200

@api.route('/api/products/<int:product_id>', methods=['DELETE'])
@login_required
def delete_product(product_id):
    if not current_user.is_admin:
        return jsonify({'error': 'Admin access required'}), 403
    
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    
    return jsonify({'message': 'Product deleted successfully'}), 200

# Cart APIs
@api.route('/api/cart', methods=['GET'])
@login_required
def get_cart():
    cart_items = Cart.query.filter_by(customer_id=current_user.id).all()
    total = sum(item.quantity * item.product.price for item in cart_items)
    
    return jsonify({
        'items': [item.to_dict() for item in cart_items],
        'total': total,
        'count': len(cart_items)
    }), 200

@api.route('/api/cart', methods=['POST'])
@login_required
def add_to_cart():
    data = request.get_json()
    product_id = data['product_id']
    quantity = data.get('quantity', 1)
    
    product = Product.query.get_or_404(product_id)
    
    if product.product_quantity < quantity:
        return jsonify({'error': 'Insufficient stock'}), 400
    
    cart_item = Cart.query.filter_by(customer_id=current_user.id, product_id=product_id).first()
    
    if cart_item:
        cart_item.quantity += quantity
    else:
        cart_item = Cart(customer_id=current_user.id, product_id=product_id, quantity=quantity)
        db.session.add(cart_item)
    
    db.session.commit()
    return jsonify(cart_item.to_dict()), 201

@api.route('/api/cart/<int:item_id>', methods=['PUT'])
@login_required
def update_cart_item(item_id):
    cart_item = Cart.query.filter_by(id=item_id, customer_id=current_user.id).first_or_404()
    data = request.get_json()
    
    if 'quantity' in data:
        if data['quantity'] <= 0:
            db.session.delete(cart_item)
        else:
            cart_item.quantity = data['quantity']
    
    db.session.commit()
    return jsonify({'message': 'Cart updated successfully'}), 200

@api.route('/api/cart/<int:item_id>', methods=['DELETE'])
@login_required
def remove_from_cart(item_id):
    cart_item = Cart.query.filter_by(id=item_id, customer_id=current_user.id).first_or_404()
    db.session.delete(cart_item)
    db.session.commit()
    
    return jsonify({'message': 'Item removed from cart'}), 200

@api.route('/api/cart/clear', methods=['DELETE'])
@login_required
def clear_cart():
    Cart.query.filter_by(customer_id=current_user.id).delete()
    db.session.commit()
    
    return jsonify({'message': 'Cart cleared successfully'}), 200

# Order APIs
@api.route('/api/orders', methods=['GET'])
@login_required
def get_orders():
    orders = Order.query.filter_by(customer_id=current_user.id).order_by(Order.created_at.desc()).all()
    return jsonify([order.to_dict() for order in orders]), 200

@api.route('/api/orders/<int:order_id>', methods=['GET'])
@login_required
def get_order(order_id):
    order = Order.query.filter_by(id=order_id, customer_id=current_user.id).first_or_404()
    return jsonify(order.to_dict()), 200

@api.route('/api/orders', methods=['POST'])
@login_required
def create_order():
    data = request.get_json()
    cart_items = Cart.query.filter_by(customer_id=current_user.id).all()
    
    if not cart_items:
        return jsonify({'error': 'Cart is empty'}), 400
    
    total_amount = sum(item.quantity * item.product.price for item in cart_items)
    order_number = f"ORD-{secrets.token_hex(8).upper()}"
    
    order = Order(
        order_number=order_number,
        total_amount=total_amount,
        customer_id=current_user.id,
        shipping_address=data.get('shipping_address'),
        billing_address=data.get('billing_address'),
        payment_method=data.get('payment_method'),
        notes=data.get('notes')
    )
    
    db.session.add(order)
    db.session.flush()
    
    for cart_item in cart_items:
        order_item = OrderItem(
            order_id=order.id,
            product_id=cart_item.product_id,
            quantity=cart_item.quantity,
            price=cart_item.product.price
        )
        db.session.add(order_item)
        
        # Update product quantity
        cart_item.product.product_quantity -= cart_item.quantity
    
    # Clear cart
    Cart.query.filter_by(customer_id=current_user.id).delete()
    
    db.session.commit()
    return jsonify(order.to_dict()), 201

@api.route('/api/orders/<int:order_id>/status', methods=['PUT'])
@login_required
def update_order_status(order_id):
    if not current_user.is_admin:
        return jsonify({'error': 'Admin access required'}), 403
    
    order = Order.query.get_or_404(order_id)
    data = request.get_json()
    
    if 'status' in data:
        order.status = data['status']
        if data['status'] == 'shipped':
            order.shipped_at = datetime.utcnow()
        elif data['status'] == 'delivered':
            order.delivered_at = datetime.utcnow()
    
    if 'payment_status' in data:
        order.payment_status = data['payment_status']
    
    db.session.commit()
    return jsonify(order.to_dict()), 200

# Address APIs
@api.route('/api/addresses', methods=['GET'])
@login_required
def get_addresses():
    addresses = Address.query.filter_by(customer_id=current_user.id).all()
    return jsonify([addr.to_dict() for addr in addresses]), 200

@api.route('/api/addresses', methods=['POST'])
@login_required
def create_address():
    data = request.get_json()
    
    address = Address(
        customer_id=current_user.id,
        street_address=data['street_address'],
        city=data['city'],
        state=data['state'],
        postal_code=data['postal_code'],
        country=data['country'],
        address_type=data.get('address_type', 'shipping'),
        is_default=data.get('is_default', False)
    )
    
    if address.is_default:
        Address.query.filter_by(customer_id=current_user.id, address_type=address.address_type).update({'is_default': False})
    
    db.session.add(address)
    db.session.commit()
    
    return jsonify(address.to_dict()), 201

@api.route('/api/addresses/<int:address_id>', methods=['PUT'])
@login_required
def update_address(address_id):
    address = Address.query.filter_by(id=address_id, customer_id=current_user.id).first_or_404()
    data = request.get_json()
    
    for field in ['street_address', 'city', 'state', 'postal_code', 'country', 'address_type', 'is_default']:
        if field in data:
            setattr(address, field, data[field])
    
    if address.is_default:
        Address.query.filter_by(customer_id=current_user.id, address_type=address.address_type).update({'is_default': False})
        address.is_default = True
    
    db.session.commit()
    return jsonify(address.to_dict()), 200

@api.route('/api/addresses/<int:address_id>', methods=['DELETE'])
@login_required
def delete_address(address_id):
    address = Address.query.filter_by(id=address_id, customer_id=current_user.id).first_or_404()
    db.session.delete(address)
    db.session.commit()
    
    return jsonify({'message': 'Address deleted successfully'}), 200

# Review APIs
@api.route('/api/products/<int:product_id>/reviews', methods=['GET'])
def get_product_reviews(product_id):
    reviews = Review.query.filter_by(product_id=product_id).order_by(Review.created_at.desc()).all()
    return jsonify([review.to_dict() for review in reviews]), 200

@api.route('/api/products/<int:product_id>/reviews', methods=['POST'])
@login_required
def create_review(product_id):
    data = request.get_json()
    
    existing_review = Review.query.filter_by(customer_id=current_user.id, product_id=product_id).first()
    if existing_review:
        return jsonify({'error': 'You have already reviewed this product'}), 400
    
    review = Review(
        customer_id=current_user.id,
        product_id=product_id,
        rating=data['rating'],
        title=data.get('title'),
        comment=data.get('comment')
    )
    
    db.session.add(review)
    db.session.commit()
    
    return jsonify(review.to_dict()), 201

# Wishlist APIs
@api.route('/api/wishlist', methods=['GET'])
@login_required
def get_wishlist():
    wishlist_items = Wishlist.query.filter_by(customer_id=current_user.id).all()
    return jsonify([item.to_dict() for item in wishlist_items]), 200

@api.route('/api/wishlist', methods=['POST'])
@login_required
def add_to_wishlist():
    data = request.get_json()
    product_id = data['product_id']
    
    existing_item = Wishlist.query.filter_by(customer_id=current_user.id, product_id=product_id).first()
    if existing_item:
        return jsonify({'error': 'Product already in wishlist'}), 400
    
    wishlist_item = Wishlist(customer_id=current_user.id, product_id=product_id)
    db.session.add(wishlist_item)
    db.session.commit()
    
    return jsonify(wishlist_item.to_dict()), 201

@api.route('/api/wishlist/<int:item_id>', methods=['DELETE'])
@login_required
def remove_from_wishlist(item_id):
    wishlist_item = Wishlist.query.filter_by(id=item_id, customer_id=current_user.id).first_or_404()
    db.session.delete(wishlist_item)
    db.session.commit()
    
    return jsonify({'message': 'Item removed from wishlist'}), 200

# Admin APIs
@api.route('/api/admin/dashboard', methods=['GET'])
@login_required
def admin_dashboard():
    if not current_user.is_admin:
        return jsonify({'error': 'Admin access required'}), 403
    
    total_customers = Customer.query.count()
    total_products = Product.query.count()
    total_orders = Order.query.count()
    pending_orders = Order.query.filter_by(status='pending').count()
    
    return jsonify({
        'total_customers': total_customers,
        'total_products': total_products,
        'total_orders': total_orders,
        'pending_orders': pending_orders
    }), 200

@api.route('/api/admin/orders', methods=['GET'])
@login_required
def admin_get_orders():
    if not current_user.is_admin:
        return jsonify({'error': 'Admin access required'}), 403
    
    orders = Order.query.order_by(Order.created_at.desc()).all()
    return jsonify([order.to_dict() for order in orders]), 200

@api.route('/api/admin/customers', methods=['GET'])
@login_required
def admin_get_customers():
    if not current_user.is_admin:
        return jsonify({'error': 'Admin access required'}), 403
    
    customers = Customer.query.all()
    return jsonify([customer.to_dict() for customer in customers]), 200