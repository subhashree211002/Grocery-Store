from flask import Flask
from flask import render_template
from flask import request, jsonify
from flask import current_app as app
from application.models import Category, Product, Managers, Users, Orders_Desc, Order_Details
from .database import db
import pandas as pd
from datetime import datetime

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
            for o in product.ords:
                db.session.delete(o)
            db.session.delete(product)
            db.session.commit()
            return jsonify(stat='success')
        else:
            return jsonify(error='Product not found')
    except Exception as e:
        db.session.rollback()
        return jsonify(error='An error occurred while deleting the product')

@app.route("/del_cat", methods=['POST'])
def del_cat():
    cid = int(request.json['cid'])
    
    try:
        category = Category.query.get(cid)
        if category is not None:
            for p in category.products:
                print(p.PID)
                db.session.delete(p) 
            db.session.delete(category)
            db.session.commit()
            return jsonify(stat='success')
        else:
            return jsonify(error='Product not found')
    except Exception as e:
        db.session.rollback()
        return jsonify(error='An error occurred while deleting the product')
    
@app.route("/<usr>/summary")
def summarize(usr):
    return render_template("summary.html", user=usr, cat=None)

@app.route("/summarize", methods = ['POST'])
def summa():
    from_date = request.json['from']
    to_date = request.json['to']
    temp = sales_graph(from_date, to_date)
    return jsonify(category_graph_data=temp[0], product_graph_data=temp[1])


#@app.route('/graph')
def sales_graph(from_date, to_date):
    if from_date is not "" and to_date is not "":
        # Convert the from and to dates to Python date objects
        from_date = datetime.strptime(from_date, '%Y-%m-%d').date()
        to_date = datetime.strptime(to_date, '%Y-%m-%d').date()
    
        # Perform a join query to fetch sales data by date
        sales_data = db.session.query(
            Orders_Desc.Date,
            Category.Name,
            Product.Name,
            Order_Details.Qty
        ).join(Order_Details, Orders_Desc.OID == Order_Details.OID)\
        .join(Product, Product.PID == Order_Details.PID)\
        .join(Category, Category.CID == Product.CID)\
        .filter(Orders_Desc.Date >= from_date, Orders_Desc.Date <= to_date)\
        .order_by(Orders_Desc.Date).all()
    else:
        # Perform a join query to fetch sales data by date
        sales_data = db.session.query(
            Orders_Desc.Date,
            Category.Name,
            Product.Name,
            Order_Details.Qty
        ).join(Order_Details, Orders_Desc.OID == Order_Details.OID)\
        .join(Product, Product.PID == Order_Details.PID)\
        .join(Category, Category.CID == Product.CID)\
        .order_by(Orders_Desc.Date).all()

    # Convert the data to a list of dictionaries for easy rendering in the template
    sales_by_date = []
    categories = []
    products = []
    cat_to_prod = {}
    prod_to_cat = {}
    for date, category, product, quantity in sales_data:
        sales_by_date.append({
            'Date': date.strftime('%Y-%m-%d'),
            'Category': category,
            'Product': product,
            'Quantity': quantity
        })
        
        if category not in categories:
            cat_to_prod[category] = []
            categories.append(category)
        elif product not in cat_to_prod[category]:
            cat_to_prod[category].append(product)
        
        if product not in products:
            products.append(product)
            
        prod_to_cat[product] = category
            
    #print(sales_data)
    #print(categories)
    #print(products)
    #print(cat_to_prod)
    #print(prod_to_cat)
    
    # Query category-wise sales using the model class directly
    c_sales = {}
    for c in categories:
        c_sales[c] = 0
    
    # Query product-wise sales using the model class directly
    p_sales = {}
    for p in products:
        p_sales[p] = 0
        
    for d, c, p, q in sales_data:
        c_sales[c] += q
        p_sales[p] += q

    print("\n\n------------")
    #print(c_sales)
    #print(p_sales)
    
    category_sales = {'Category':[], 'TotalSales':[]}
    for c in c_sales:
        category_sales['Category'].append(c)
        category_sales['TotalSales'].append(c_sales[c])
        
    product_sales = {'Product':[], 'Category':[], 'TotalSales':[]}
    for p in p_sales:
        product_sales['Product'].append(p)
        product_sales['Category'].append(prod_to_cat[p])
        product_sales['TotalSales'].append(p_sales[p])
    
    # Convert the data to pandas DataFrame for easier manipulation
    category_sales_df = pd.DataFrame(category_sales, columns=['Category', 'TotalSales'])
    product_sales_df = pd.DataFrame(product_sales, columns=['Product', 'Category', 'TotalSales'])

    print(category_sales_df)
    print(product_sales_df)
    
    
    #category_data = {category: cat_to_prod[category] for category in categories}
    #category_data = {category: [product_sales_df.loc[product_sales_df['Category'] == category, 'TotalSales'].tolist()]
     #               for category in categories}

    # Convert the data to a format suitable for the graphs
    category_sales_data = {
        'x': category_sales_df['Category'].tolist(),
        'y': category_sales_df['TotalSales'].tolist(),
        'type': 'bar',
        'name': 'Category Sales'
    }

    product_sales_data = {
        'x': product_sales_df['Product'].tolist(),
        'y': product_sales_df['TotalSales'].tolist(),
        'type': 'bar',
        'name': 'Product Sales'
    }

    category_graph_data = [category_sales_data]
    product_graph_data = [product_sales_data]

    return category_graph_data, product_graph_data



