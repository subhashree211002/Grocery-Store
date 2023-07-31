from flask import Flask
from flask import render_template
from flask import request, jsonify
from flask import current_app as app
from application.models import Category, Product, Managers, Users, Orders_Desc, Order_Details
from .database import db
from datetime import datetime

@app.route("/<usr>/cart_addition/prod_<pid>")
def define_item_qty(usr, pid):
    p = Product.query.filter(Product.PID == pid).first()
    c = Category.query.filter(Category.CID == p.CID).first()
    return render_template("add_to_cart.html", user=usr, prod=p, cat = c)

@app.route("/add_item", methods=['POST'])
def add_to_cart():
    uname = request.json['uid']
    pid = request.json['pid']
    qty = request.json['qty']

    status = ""
    u = Users.query.filter(Users.Uname == uname).first()
    active_order = None
    for o in u.orders:
        if o.Status == 1:
            active_order = o
            print(active_order.OID)
    if active_order is None:
        try:
            new_order = Orders_Desc(Status = 1, Uname = uname)
            db.session.add(new_order)
            db.session.flush()
            
            new_line_item = Order_Details(OID = new_order.OID, PID = pid, Qty = qty)
            db.session.add(new_line_item)
            db.session.flush()
        except:
            status = "Invalid addition"
            print("Rolling back")
            db.session.rollback()
        else:
            status="success"
            db.session.commit()
            print("Commit")
    else:
        try:            
            new_line_item = Order_Details(OID = active_order.OID, PID = pid, Qty = qty)
            db.session.add(new_line_item)
            db.session.flush()
        except:
            status = "This item exists in your cart\n You can change your quantity by editing the cart"
            print("Rolling back")
            db.session.rollback()
        else:
            status="success"
            db.session.commit()
            print("Commit")
            
    return jsonify(stat=status)

@app.route("/<usr>/cart")
def show_cart(usr):
    u = Users.query.filter(Users.Uname == usr).first()
    active_order = None
    for o in u.orders:
        if o.Status == 1:
            active_order = o
    if active_order is None:
        return render_template("cart.html", user=usr, order=None)
    else:
        details = None
        #details = Product.query.join(Order_Details, Product.PID ==  Order_Details.PID).filter(Order_Details.OID == active_order.OID)
        details = db.session.query(Order_Details, Product).join(Product, Product.PID ==  Order_Details.PID).filter(Order_Details.OID == active_order.OID).all()
        if len(details) == 0:
            return render_template("cart.html", user=usr, order=None)    
        return render_template("cart.html", user=usr, order=details)
    
@app.route("/update_item", methods = ['POST'])
def update_order():
    oid = request.json['oid']
    pid = request.json['pid']
    qty = request.json['qty']

    status = ""
    item = Order_Details.query.filter(Order_Details.OID == oid, Order_Details.PID == pid).first()
    
    if item is None:
        status = "failure"
    else:
        try:
            item.Qty = qty;
            db.session.flush()

        except Exception as e:
            status = "Invalid request"
            print("Rolling back")
            
        else:
            status="success"
            db.session.commit()
            print("Commit")
            
    return jsonify(stat=status)

@app.route("/del_item", methods = ['POST'])
def del_from_order():
    oid = request.json['oid']
    pid = request.json['pid']

    item = Order_Details.query.filter(Order_Details.OID == oid, Order_Details.PID == pid).first()

    try:
        if item is not None:
            
            db.session.delete(item)
            db.session.commit()
            return jsonify(stat='success')
        else:
            return jsonify(error='Product not found')
    except Exception as e:
        db.session.rollback()
        return jsonify(error='An error occurred while deleting the product')
    
@app.route("/checkout_cart", methods = ['POST'])
def checkout():
    oid = request.json['oid']
    iso_datetime = request.json['date']
    datetime_obj = datetime.strptime(iso_datetime, '%Y-%m-%dT%H:%M:%S.%fZ')

    status = ""
    order = Orders_Desc.query.filter(Orders_Desc.OID == oid).first()
    
    if order is None:
        status = "failure"
    else:
        try:
            order.Status = 0
            order.Date = datetime_obj
            db.session.flush()

        except Exception as e:
            status = "Invalid request"
            print("Rolling back")
            
        else:
            status="success"
            db.session.commit()
            print("Commit")
            
    return jsonify(stat=status)