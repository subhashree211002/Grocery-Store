from .database import db

class Category(db.Model):
    # Table for product categories
    __tablename__ = 'Category'
    CID = db.Column(db.Integer, autoincrement=True, primary_key=True)
    Name = db.Column(db.String(collation='NOCASE'), unique=True, nullable=False)

    # Establishing the relationship from Category to Product
    products = db.relationship("Product", back_populates="cat", cascade='all, delete-orphan', passive_deletes=True)
    
class Product(db.Model):
    # Table for individual products
    __tablename__ = 'Product'
    PID = db.Column(db.Integer, autoincrement=True, primary_key=True)
    Name = db.Column(db.String(collation='NOCASE'), unique=True, nullable=False)
    Price = db.Column(db.Float, nullable=False)
    Unit = db.Column(db.String, nullable=False)
    Stock = db.Column(db.Integer, nullable=False)
    CID = db.Column(db.Integer, db.ForeignKey('Category.CID', ondelete='CASCADE'), nullable=False)
    
    # Establishing the relationship from Product to Category
    cat = db.relationship("Category", back_populates="products")
    
class Managers(db.Model):
    # Table for managers
    __tablename__ = 'Managers'
    Uname = db.Column(db.String, primary_key=True)
    Pwd = db.Column(db.String, nullable=False)
    
class Users(db.Model):
    # Table for users
    __tablename__ = 'Users'
    Uname = db.Column(db.String, primary_key=True)
    Pwd = db.Column(db.String, nullable=False)
    
    # Establishing the relationship from Users to Order_Desc
    orders = db.relationship("Orders_Desc", back_populates="user", cascade='all, delete-orphan', passive_deletes=True)
    
class Orders_Desc(db.Model):
    # Table for order description
    __tablename__ = 'Orders_Desc'
    OID = db.Column(db.Integer, autoincrement=True, primary_key=True)
    Date = db.Column(db.Date)
    Status = db.Column(db.Integer, nullable=False, default=0)  # Change default value to 0
    Uname = db.Column(db.String, db.ForeignKey('Users.Uname', ondelete='CASCADE'), nullable=False)
    
    # Establishing the relationship from Order_Desc to Users
    user = db.relationship("Users", back_populates="orders")
    
    # Establishing the relationship from Order_Desc to Order_Details
    products = db.relationship("Order_Details", back_populates="order", cascade='all, delete-orphan', passive_deletes=True)

class Order_Details(db.Model):
    # Table for order details
    __tablename__ = 'Order_Details'
    OID = db.Column(db.Integer, db.ForeignKey('Orders_Desc.OID', ondelete='CASCADE'), primary_key=True)
    PID = db.Column(db.Integer, db.ForeignKey('Product.PID', ondelete='CASCADE'), primary_key=True)
    Qty = db.Column(db.Integer, nullable=False)
    
    # Define the composite primary key constraint
    __table_args__ = (db.PrimaryKeyConstraint('OID', 'PID'),)
    
    # Establishing the relationship from Order_Details to Order_Desc
    order = db.relationship("Orders_Desc", back_populates="products")