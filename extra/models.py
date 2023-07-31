import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, Float, String, Date, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import Session
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Category(Base):
    # Table for product categories
    __tablename__ = 'Category'
    CID = Column(Integer, autoincrement=True, primary_key=True)
    Name = Column(String(collation='NOCASE'), unique=True, nullable=False)

    # Establishing the relationship from Category to Product
    products = relationship("Product", back_populates="cat")
    
class Product(Base):
    # Table for individual products
    __tablename__ = 'Product'
    PID = Column(Integer, autoincrement=True, primary_key=True)
    Name = Column(String(collation='NOCASE'), unique=True, nullable=False)
    Price = Column(Float, nullable=False)
    Unit = Column(String, nullable=False)
    Stock = Column(Integer, nullable=False)
    CID = Column(Integer, ForeignKey('Category.CID'), nullable=False)
    
    # Establishing the relationship from Product to Category
    cat = relationship("Category", back_populates="products")
    
class Managers(Base):
    # Table for managers
    __tablename__ = 'Managers'
    Uname = Column(String, primary_key=True)
    Pwd = Column(String, nullable=False)
    
class Users(Base):
    # Table for users
    __tablename__ = 'Users'
    Uname = Column(String, primary_key=True)
    Pwd = Column(String, nullable=False)
    
    # Establishing the relationship from Users to Order_Desc
    orders = relationship("Orders_Desc", back_populates="user")
    
class Orders_Desc(Base):
    # Table for order description
    __tablename__ = 'Orders_Desc'
    OID = Column(Integer, autoincrement=True, primary_key=True)
    Date = Column(Date)
    Status = Column(Integer, nullable=False, default=0)  # Change default value to 0
    Uname = Column(String, ForeignKey('Users.Uname'), nullable=False)
    
    # Establishing the relationship from Order_Desc to Users
    user = relationship("Users", back_populates="orders")
    
    # Establishing the relationship from Order_Desc to Order_Details
    products = relationship("Order_Details", back_populates="order")

class Order_Details(Base):
    # Table for order details
    __tablename__ = 'Order_Details'
    OID = Column(Integer, ForeignKey('Orders_Desc.OID'), primary_key=True)
    PID = Column(Integer, ForeignKey('Product.PID'), primary_key=True)
    Qty = Column(Integer, nullable=False)
    
    # Define the composite primary key constraint
    __table_args__ = (PrimaryKeyConstraint('OID', 'PID'),)
    
    # Establishing the relationship from Order_Details to Order_Desc
    order = relationship("Orders_Desc", back_populates="products")

engine = create_engine("sqlite:///./grocery_store.db")

if __name__ == "__main__":
    with Session(engine, autoflush=False) as session:
        session.begin()
        categories = session.query(Category).all()
        
        for c in categories:
            print(c.CID, c.Name, end = " ")
            for p in c.products:
                print(p.Name, end = " ")
            print()
            
        """try:
            new_cat = Category(Name="Meat")
            session.add(new_cat)
            session.flush()
            print("---get category id----")
            print(new_cat.CID)
            products = Product(Name="Chicken", Price=250, Unit="Rs/kg", Stock=20, CID=new_cat.CID)
            session.add(products)
        except:
            print("Rolling back")
            session.rollback()
            raise
        else:
            print("Commit")
            session.commit()"""