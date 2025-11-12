#!/usr/bin/env python3
"""
Database migration script for new Product schema
Run this to update existing database with new Product fields
"""

from website import create_app, db
from website.models import Product

def migrate_database():
    app = create_app()
    
    with app.app_context():
        # Create all tables with new schema
        db.create_all()
        
        # Update existing products to have legacy id field match product_id
        products = Product.query.all()
        for product in products:
            if product.id is None:
                product.id = product.product_id
        
        db.session.commit()
        print("Database migration completed successfully!")

if __name__ == "__main__":
    migrate_database()