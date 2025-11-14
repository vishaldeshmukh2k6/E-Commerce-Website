// Main JavaScript file for E-Commerce Store

// API base URL
const API_BASE_URL = '/api';

// Utility functions
function showAlert(message, type = 'info') {
    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type} alert-dismissible fade show`;
    alertDiv.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    document.querySelector('main').insertBefore(alertDiv, document.querySelector('main').firstChild);
    
    setTimeout(() => {
        alertDiv.remove();
    }, 5000);
}

function formatPrice(price) {
    return new Intl.NumberFormat('en-US', {
        style: 'currency',
        currency: 'USD'
    }).format(price);
}

function formatDate(dateString) {
    return new Date(dateString).toLocaleDateString();
}

// API helper functions
async function apiRequest(endpoint, options = {}) {
    try {
        const response = await fetch(`${API_BASE_URL}${endpoint}`, {
            headers: {
                'Content-Type': 'application/json',
                ...options.headers
            },
            ...options
        });
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        return await response.json();
    } catch (error) {
        console.error('API request failed:', error);
        showAlert('An error occurred. Please try again.', 'danger');
        throw error;
    }
}

// Initialize page-specific functionality
document.addEventListener('DOMContentLoaded', function() {
    const currentPage = window.location.pathname;
    
    // Initialize based on current page
    if (currentPage === '/' || currentPage === '/home') {
        initHomePage();
    } else if (currentPage === '/products') {
        initProductsPage();
    } else if (currentPage.startsWith('/product/')) {
        initProductDetailPage();
    } else if (currentPage === '/cart') {
        initCartPage();
    } else if (currentPage === '/checkout') {
        initCheckoutPage();
    } else if (currentPage === '/login') {
        initLoginPage();
    } else if (currentPage === '/register') {
        initRegisterPage();
    } else if (currentPage === '/profile') {
        initProfilePage();
    } else if (currentPage === '/wishlist') {
        initWishlistPage();
    } else if (currentPage === '/categories') {
        initCategoriesPage();
    } else if (currentPage === '/admin/dashboard') {
        initAdminDashboard();
    }
});

// Page initialization functions (placeholders)
function initHomePage() {
    console.log('Home page initialized');
    // Load featured products, etc.
}

function initProductsPage() {
    console.log('Products page initialized');
    // Load products, setup filters, etc.
}

function initProductDetailPage() {
    console.log('Product detail page initialized');
    // Load product details, reviews, etc.
}

function initCartPage() {
    console.log('Cart page initialized');
    // Load cart items, setup quantity controls, etc.
}

function initCheckoutPage() {
    console.log('Checkout page initialized');
    // Setup form validation, payment processing, etc.
}

function initLoginPage() {
    console.log('Login page initialized');
    // Setup login form
}

function initRegisterPage() {
    console.log('Register page initialized');
    // Setup registration form
}

function initProfilePage() {
    console.log('Profile page initialized');
    // Load user profile, orders, addresses, etc.
}

function initWishlistPage() {
    console.log('Wishlist page initialized');
    // Load wishlist items
}

function initCategoriesPage() {
    console.log('Categories page initialized');
    // Load categories
}

function initAdminDashboard() {
    console.log('Admin dashboard initialized');
    // Load dashboard stats, recent orders, etc.
}