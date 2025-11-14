from flask import Blueprint, render_template, jsonify

views = Blueprint('views', __name__)

# Frontend Routes
@views.route('/')
def home():
    return render_template('index.html')

@views.route('/products')
def products():
    return render_template('products.html')

@views.route('/product/<int:product_id>')
def product_detail(product_id):
    return render_template('product_detail.html')

@views.route('/cart')
def cart():
    return render_template('cart.html')

@views.route('/checkout')
def checkout():
    return render_template('checkout.html')

@views.route('/login')
def login():
    return render_template('login.html')

@views.route('/register')
def register():
    return render_template('register.html')

@views.route('/profile')
def profile():
    return render_template('profile.html')

@views.route('/wishlist')
def wishlist():
    return render_template('wishlist.html')

@views.route('/categories')
def categories():
    return render_template('categories.html')

@views.route('/about')
def about():
    return render_template('about.html')

@views.route('/contact')
def contact():
    return render_template('contact.html')

# Admin Routes
@views.route('/admin/dashboard')
def admin_dashboard():
    return render_template('admin_dashboard.html')

@views.route('/admin/products')
def admin_products():
    return render_template('admin_products.html')

@views.route('/admin/orders')
def admin_orders():
    return render_template('admin_orders.html')

@views.route('/admin/customers')
def admin_customers():
    return render_template('admin_customers.html')

# API Status Routes
@views.route('/api')
def api_info():
    return jsonify({
        'message': 'E-Commerce API Server',
        'version': '1.0.0',
        'endpoints': {
            'auth': '/api/auth/*',
            'products': '/api/products',
            'categories': '/api/categories',
            'cart': '/api/cart',
            'orders': '/api/orders',
            'addresses': '/api/addresses',
            'reviews': '/api/products/{id}/reviews',
            'wishlist': '/api/wishlist',
            'admin': '/api/admin/*'
        }
    }), 200

@views.route('/health')
def health_check():
    return jsonify({'status': 'healthy'}), 200