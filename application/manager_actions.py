from flask import Flask
from flask import render_template
from flask import request, jsonify
from flask import current_app as app
from application.models import Category, Product, Managers, Users, Orders_Desc, Order_Details
from .database import db

def is_number(value):
    try:
        float(value)
        return True
    except (ValueError, TypeError):
        return False
    

def is_int(value):
    try:
        int(value)  # You can use int() for integers only
        return True
    except (ValueError, TypeError):
        return False
    
@app.route("/<usr>/add_category")
def create_category_page(usr):
    return render_template("create_edit_cat.html", user=usr, cat=None)

@app.route("/<usr>/add_prod/cat_<cat>")
def create_product_page(usr, cat):
    c = Category.query.filter(Category.CID == cat).first()
    return render_template("create_edit_prod.html", user=usr, cat = c, prod= None)

@app.route("/<usr>/edit_category/cat_<cat>")
def edit_category_page(usr, cat):
    c = Category.query.filter(Category.CID == cat).first()
    return render_template("create_edit_cat.html", user=usr, cat = c)

@app.route("/<usr>/edit_product/cat_<cat>/prod_<pid>")
def edit_product_page(usr, cat, pid):
    p = Product.query.filter(Product.PID == pid).first()
    c = Category.query.filter(Category.CID == cat).first()
    return render_template("create_edit_prod.html", user=usr, cat = c, prod = p)

@app.route("/add_cat_val", methods = ['POST'])
def create_category():
    name = request.json['name']
    
    status = ""
    if len(name) == 0:
        status = "Invalid category name"
    else:
        try:
            new_cat = Category(Name=name)
            db.session.add(new_cat)
            db.session.flush()
        except Exception as e:
            status = "Invalid category name - it already exists"
            print("Rolling back", e)
            db.session.rollback()
        else:
            status="success"
            db.session.commit()
            print("Commit")
    
    # Return the updated value as a JSON response
    return jsonify(stat=status)

@app.route("/add_prod_val", methods = ['POST'])
def create_product():
    pname = request.json['pname']
    punit = request.json['punit']
    prate = request.json['prate']
    pqt = request.json['pqt']
    cat_id = request.json['cat_id']
    
    
    status = ""
    if len(pname) == 0:
        status = "Product name cannot be null"
    elif punit == "Open this select menu":
        status = "'Units' field is a required field"
    elif not is_number(prate):
        status = "Rate should be a number, should not be empty"
    elif not is_int(pqt):
        status = "Quantity should be an integer, should not be empty"
    else:
        try:
            new_prod = Product(Name=pname, Unit=punit, Price=prate, Stock=pqt, CID=cat_id)
            db.session.add(new_prod)
            db.session.flush()
            print("here1")
        except:
            status = "Invalid product name already exists"
            print("Rolling back")
            db.session.rollback()
        else:
            status="success"
            db.session.commit()
            print("Commit")
    
    # Return the updated value as a JSON response
    return jsonify(stat=status)

@app.route("/update_cat_val", methods = ['POST'])
def update_category():
    name = request.json['name']
    cid = int(request.json['cid'])
    
    status = ""
    
    cat = Category.query.filter(Category.Name == name).first()

    if len(name) == 0 or cat is not None:
        status = "Invalid category name - null or already exists"
    else:
        try:
            cat = Category.query.filter(Category.CID == cid).first()
            cat.Name = name

        except Exception as e:
            status = "Invalid request"
            print("Rolling back")
            
        else:
            status="success"
            db.session.commit()
            print("Commit")
    
    # Return the updated value as a JSON response
    return jsonify(stat=status)

@app.route("/update_prod_val", methods = ['POST'])
def update_product():
    pid = request.json['pid']
    pname = request.json['pname']
    punit = request.json['punit']
    prate = request.json['prate']
    pqt = request.json['pqt']
    cat_id = request.json['cat_id']
    
    status = ""
    
    if len(pname) == 0:
        status = "Product name cannot be null"
    elif punit == "Open this select menu":
        status = "'Units' field is a required field"
    elif not is_number(prate):
        status = "Rate should be a number, should not be empty"
    elif not is_int(pqt):
        status = "Quantity should be an integer, should not be empty"
    else:
        try:
            prod = Product.query.filter(Product.PID == pid).first()
            prod.Name = pname
            prod.Unit = punit
            prod.Price = float(prate)
            prod.Stock = int(pqt)
            prod.CID = int(cat_id)

        except Exception as e:
            status = "Another object with same name exists"
            print("Rolling back")
            
        else:
            status="success"
            db.session.commit()
            print("Commit")
    
    # Return the updated value as a JSON response
    return jsonify(stat=status)

@app.route("/del_prod", methods=['POST'])
def del_prod():
    pid = int(request.json['pid'])
    
    try:
        product = Product.query.get(pid)
        if product is not None:
            
            db.session.delete(product)
            db.session.commit()
            return jsonify(stat='success')
        else:
            return jsonify(error='Product not found')
    except Exception as e:
        db.session.rollback()
        return jsonify(error='An error occurred while deleting the product')
    return

@app.route("/del_cat", methods=['POST'])
def del_cat():
    cid = int(request.json['cid'])
    
    try:
        category = Category.query.get(cid)
        if category is not None:
            
            db.session.delete(category)
            db.session.commit()
            return jsonify(stat='success')
        else:
            return jsonify(error='Product not found')
    except Exception as e:
        db.session.rollback()
        return jsonify(error='An error occurred while deleting the product')
    return

