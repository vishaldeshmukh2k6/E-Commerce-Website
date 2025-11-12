# ⚡🛒 Flask E-Commerce API | Advanced Backend System 🐍

<p align="center">
    <em>🧠 A production-ready E-Commerce REST API built with <b>Flask</b> — featuring authentication, admin controls, payments, and comprehensive product management.</em>
</p>

---

## 🪪 License  

📄 Licensed under the **MIT License** — use, modify, and distribute freely with proper credit.  
💬 *"Code freely. Share wisely."*

---

## 🏬 Overview  

This project is a **Flask-based E-Commerce REST API** that delivers a complete backend solution for online shopping platforms — with **user management**, **product control**, **order processing**, and **comprehensive admin features**.  
Optimized for performance using **Gunicorn**, designed for scalability, and built for real-world deployment.

> 🎨 **Frontend Coming Soon!** A modern React/Vue.js frontend application is currently in development to provide a complete full-stack e-commerce solution.  

---

## ✨ Key Features  

### 👥 Customer Features
- 🔐 **Secure Registration & Authentication**
- 👤 **Profile Management**
- 🔍 **Advanced Product Search & Filtering**
- 🛒 **Shopping Cart Management**
- 📦 **Order History & Tracking**
- 📍 **Multiple Address Management**
- ⭐ **Product Reviews & Ratings**
- ❤️ **Wishlist Functionality**

### 🧑💼 Admin Features
- 📊 **Admin Dashboard with Analytics**
- 📦 **Complete Product Management (CRUD)**
- 🏷️ **Category Management**
- 📋 **Order Management & Status Updates**
- 👥 **Customer Management**
- 📈 **Sales & Inventory Tracking**

### ⚙️ System Features
- 🧰 **RESTful API Architecture**
- 🔒 **Session-based Authentication**
- 📄 **Pagination Support**
- 🔍 **Advanced Search & Filtering**
- 🌐 **CORS Enabled**
- 💾 **SQLite Database (easily switchable to PostgreSQL)**
- 📚 **Comprehensive API Documentation**
- 🧪 **Postman Collection Included**

---

## 🧱 Tech Stack  

| 🧩 Layer | 🔧 Technology |
|:--------:|:--------------|
| 🧠 **Backend** | Flask (Python) |
| 🚀 **Server** | Gunicorn WSGI |
| 🗄️ **Database** | SQLite / PostgreSQL |
| 🔐 **Authentication** | Flask-Login (Session-based) |
| 🌐 **API** | RESTful JSON API |
| 🧭 **Version Control** | Git & GitHub |

---

## 📋 Database Schema

### Core Models
- **Customer** - User accounts with profile information
- **Category** - Product categorization
- **Product** - Complete product information with ratings
- **Cart** - Shopping cart management
- **Order** - Order processing and tracking
- **OrderItem** - Individual order line items
- **Address** - Customer address management
- **Review** - Product reviews and ratings
- **Wishlist** - Save products for later

---

## 🚀 Quick Start  

### 1️⃣ Clone & Setup
```bash
git clone https://github.com/vishaldeshmukh2k6/E-Commerce-Website
cd E-Ecommerce-Website
pip install -r requirements.txt
```

### 2️⃣ Initialize Database
```bash
python fix_db.py
```

### 3️⃣ Run Development Server
```bash
flask run
# or
python main.py
```

### 4️⃣ Run Production Server
```bash
gunicorn -w 4 -b 0.0.0.0:5000 main:app
```

---

## 📡 API Endpoints

### Base URL: `http://localhost:5000`

### 🔐 Authentication
- `POST /api/auth/register` - User registration
- `POST /api/auth/login` - User login
- `POST /api/auth/logout` - User logout
- `GET /api/auth/profile` - Get user profile
- `PUT /api/auth/profile` - Update user profile

### 🏷️ Categories
- `GET /api/categories` - Get all categories
- `POST /api/categories` - Create category (Admin)
- `PUT /api/categories/{id}` - Update category (Admin)

### 📦 Products
- `GET /api/products` - Get products (with pagination & filters)
- `GET /api/products/{id}` - Get single product
- `POST /api/products` - Create product (Admin)
- `PUT /api/products/{id}` - Update product (Admin)
- `DELETE /api/products/{id}` - Delete product (Admin)

### 🛒 Shopping Cart
- `GET /api/cart` - Get cart items
- `POST /api/cart` - Add to cart
- `PUT /api/cart/{item_id}` - Update cart item
- `DELETE /api/cart/{item_id}` - Remove from cart
- `DELETE /api/cart/clear` - Clear cart

### 📋 Orders
- `GET /api/orders` - Get user orders
- `GET /api/orders/{id}` - Get single order
- `POST /api/orders` - Create order from cart
- `PUT /api/orders/{id}/status` - Update order status (Admin)

### 📍 Addresses
- `GET /api/addresses` - Get user addresses
- `POST /api/addresses` - Create address
- `PUT /api/addresses/{id}` - Update address
- `DELETE /api/addresses/{id}` - Delete address

### ⭐ Reviews
- `GET /api/products/{id}/reviews` - Get product reviews
- `POST /api/products/{id}/reviews` - Create review

### ❤️ Wishlist
- `GET /api/wishlist` - Get wishlist
- `POST /api/wishlist` - Add to wishlist
- `DELETE /api/wishlist/{item_id}` - Remove from wishlist

### 🧑💼 Admin
- `GET /api/admin/dashboard` - Admin dashboard stats
- `GET /api/admin/orders` - All orders (Admin)
- `GET /api/admin/customers` - All customers (Admin)

---

## 📚 Documentation

- **API Documentation**: `API_DOCUMENTATION.md`
- **Postman Collection**: `E-Commerce_API_Collection.postman_collection.json`

### Import Postman Collection
1. Open Postman
2. Click "Import"
3. Select `E-Commerce_API_Collection.postman_collection.json`
4. Set environment variable `base_url` to `http://localhost:5001`

---

## 🔧 Configuration

### Environment Variables
```bash
export FLASK_APP=main.py
export FLASK_ENV=development
export SECRET_KEY=your-secret-key
```

### Database Configuration
- **Development**: SQLite (`instance/database.sqlite3`)
- **Production**: Configure PostgreSQL in `__init__.py`

---

## 🧪 Testing

### Using Postman
1. Import the provided Postman collection
2. Start with user registration
3. Login to get session authentication
4. Test all endpoints

### Sample API Calls
```bash
# Register user
curl -X POST http://localhost:5001/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","username":"testuser","password":"password123"}'

# Login
curl -X POST http://localhost:5001/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"password123"}'

# Get products
curl -X GET http://localhost:5001/api/products
```

---

## 🚀 Deployment

### Using Gunicorn
```bash
gunicorn -w 4 -b 0.0.0.0:5001 main:app
```

### Using Docker (Coming Soon)
```bash
docker build -t ecommerce-api .
docker run -p 5001:5001 ecommerce-api
```

---

## 🔒 Security Features

- **Password Hashing** with Werkzeug
- **Session-based Authentication**
- **CORS Protection**
- **Input Validation**
- **SQL Injection Prevention**
- **Admin Role Protection**

---

## 📈 Performance Features

- **Database Indexing**
- **Pagination for Large Datasets**
- **Optimized Queries**
- **Gunicorn Multi-worker Support**
- **Connection Pooling Ready**

---

## 🧩 Coming Soon 🚧

1. 🎨 **Frontend Application**
2. 🐳 **Docker Support**
3. 🔐 **JWT Authentication**
4. 💳 **Payment Gateway Integration**
5. 📧 **Email Notifications**
6. 📱 **Mobile App Support**
7. 🤖 **AI Product Recommendations**
8. 📊 **Advanced Analytics**
9. 🔍 **Elasticsearch Integration**

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

---

## 📞 Support

For support and questions:
- 📧 Email: vishaldeshmuk143@gmail.com
- 📖 Documentation: `API_DOCUMENTATION.md`
- 🐛 Issues: GitHub Issues

---

## 🎯 Use Cases

Perfect for:
- 🛍️ **E-commerce Websites**
- 📱 **Mobile Shopping Apps**
- 🏪 **Multi-vendor Marketplaces**
- 📦 **Inventory Management Systems**
- 🛒 **B2B/B2C Platforms**