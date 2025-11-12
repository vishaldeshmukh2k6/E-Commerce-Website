# E-Commerce API Documentation

## Base URL
```
http://localhost:5001
```

## Authentication
Most endpoints require authentication. Use session-based authentication after login.

## API Endpoints

### Authentication

#### Register User
```http
POST /api/auth/register
Content-Type: application/json

{
  "email": "user@example.com",
  "username": "username",
  "password": "password",
  "first_name": "John",
  "last_name": "Doe",
  "phone": "+1234567890"
}
```

#### Login
```http
POST /api/auth/login
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "password"
}
```

#### Logout
```http
POST /api/auth/logout
```

#### Get Profile
```http
GET /api/auth/profile
```

#### Update Profile
```http
PUT /api/auth/profile
Content-Type: application/json

{
  "first_name": "John",
  "last_name": "Doe",
  "phone": "+1234567890"
}
```

### Categories

#### Get All Categories
```http
GET /api/categories
```

#### Create Category (Admin Only)
```http
POST /api/categories
Content-Type: application/json

{
  "name": "Electronics",
  "description": "Electronic devices and accessories",
  "image": "https://example.com/image.jpg"
}
```

#### Update Category (Admin Only)
```http
PUT /api/categories/{id}
Content-Type: application/json

{
  "name": "Updated Electronics",
  "description": "Updated description",
  "is_active": true
}
```

### Products

#### Get All Products
```http
GET /api/products?page=1&per_page=20&category_id=1&search=phone&featured=true
```

#### Get Single Product
```http
GET /api/products/{id}
```

#### Create Product (Admin Only)
```http
POST /api/products
Content-Type: application/json

{
  "product_name": "iPhone 15",
  "description": "Latest iPhone model",
  "product_quantity": 100,
  "price": 999.99,
  "old_price": 1099.99,
  "vendor": "Apple",
  "product_img": "https://example.com/iphone.jpg",
  "sku": "IPH15-001",
  "weight": 0.2,
  "dimensions": "6.1 x 2.8 x 0.3 inches",
  "category_id": 1,
  "is_featured": true,
  "flash_sale": false,
  "discount_percentage": 10
}
```

#### Update Product (Admin Only)
```http
PUT /api/products/{id}
Content-Type: application/json

{
  "product_name": "Updated iPhone 15",
  "price": 899.99,
  "product_quantity": 50
}
```

#### Delete Product (Admin Only)
```http
DELETE /api/products/{id}
```

### Cart

#### Get Cart
```http
GET /api/cart
```

#### Add to Cart
```http
POST /api/cart
Content-Type: application/json

{
  "product_id": 1,
  "quantity": 2
}
```

#### Update Cart Item
```http
PUT /api/cart/{item_id}
Content-Type: application/json

{
  "quantity": 3
}
```

#### Remove from Cart
```http
DELETE /api/cart/{item_id}
```

#### Clear Cart
```http
DELETE /api/cart/clear
```

### Orders

#### Get All Orders
```http
GET /api/orders
```

#### Get Single Order
```http
GET /api/orders/{id}
```

#### Create Order
```http
POST /api/orders
Content-Type: application/json

{
  "shipping_address": "123 Main St, City, State 12345",
  "billing_address": "123 Main St, City, State 12345",
  "payment_method": "credit_card",
  "notes": "Please deliver after 5 PM"
}
```

#### Update Order Status (Admin Only)
```http
PUT /api/orders/{id}/status
Content-Type: application/json

{
  "status": "shipped",
  "payment_status": "paid"
}
```

### Addresses

#### Get All Addresses
```http
GET /api/addresses
```

#### Create Address
```http
POST /api/addresses
Content-Type: application/json

{
  "street_address": "123 Main Street",
  "city": "New York",
  "state": "NY",
  "postal_code": "10001",
  "country": "USA",
  "address_type": "shipping",
  "is_default": true
}
```

#### Update Address
```http
PUT /api/addresses/{id}
Content-Type: application/json

{
  "street_address": "456 Oak Avenue",
  "is_default": false
}
```

#### Delete Address
```http
DELETE /api/addresses/{id}
```

### Reviews

#### Get Product Reviews
```http
GET /api/products/{product_id}/reviews
```

#### Create Review
```http
POST /api/products/{product_id}/reviews
Content-Type: application/json

{
  "rating": 5,
  "title": "Great product!",
  "comment": "I love this product. Highly recommended!"
}
```

### Wishlist

#### Get Wishlist
```http
GET /api/wishlist
```

#### Add to Wishlist
```http
POST /api/wishlist
Content-Type: application/json

{
  "product_id": 1
}
```

#### Remove from Wishlist
```http
DELETE /api/wishlist/{item_id}
```

### Admin

#### Admin Dashboard
```http
GET /api/admin/dashboard
```

#### Get All Orders (Admin)
```http
GET /api/admin/orders
```

#### Get All Customers (Admin)
```http
GET /api/admin/customers
```

## Response Format

### Success Response
```json
{
  "data": {},
  "message": "Success message"
}
```

### Error Response
```json
{
  "error": "Error message"
}
```

## Status Codes

- `200` - Success
- `201` - Created
- `400` - Bad Request
- `401` - Unauthorized
- `403` - Forbidden
- `404` - Not Found
- `500` - Internal Server Error

## Order Status Values

- `pending` - Order placed, awaiting confirmation
- `confirmed` - Order confirmed, preparing for shipment
- `shipped` - Order shipped
- `delivered` - Order delivered
- `cancelled` - Order cancelled

## Payment Status Values

- `pending` - Payment pending
- `paid` - Payment successful
- `failed` - Payment failed
- `refunded` - Payment refunded