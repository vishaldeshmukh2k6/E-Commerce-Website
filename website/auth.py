from flask import Blueprint, jsonify

auth = Blueprint('auth', __name__)

# All authentication is now handled in api.py
# These routes redirect to API endpoints

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    return jsonify({
        'message': 'Use POST /api/auth/register for user registration',
        'required_fields': ['email', 'username', 'password'],
        'optional_fields': ['first_name', 'last_name', 'phone']
    }), 200

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return jsonify({
        'message': 'Use POST /api/auth/login for authentication',
        'required_fields': ['email', 'password']
    }), 200

@auth.route('/logout', methods=['GET', 'POST'])
def log_out():
    return jsonify({
        'message': 'Use POST /api/auth/logout to logout'
    }), 200

@auth.route('/profile/<int:customer_id>')
def profile(customer_id):
    return jsonify({
        'message': 'Use GET /api/auth/profile to view profile'
    }), 200