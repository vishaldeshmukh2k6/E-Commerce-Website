from flask import Blueprint, jsonify

views = Blueprint('views', __name__)

@views.route('/')
def home():
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