from flask import Flask
from flask import render_template
from flask import request, jsonify
from flask import current_app as app
from application.models import Category, Product, Managers, Users, Orders_Desc, Order_Details
from .database import db
import re
import application.manager_actions
import application.user_actions


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login")
def login_page():
    return render_template("login.html")

@app.route('/validate/<usr_type>', methods=['POST'])
def validate_login(usr_type):
    data = request.json
    uname = data['uname']
    pwd = data['pwd']
    
    users = []
    if usr_type == "manager":
        users = Managers.query.filter(
            db.and_(
                Managers.Uname == uname,
                Managers.Pwd == pwd
            )
        ).all()
    elif usr_type == "user":
        users = Users.query.filter(
            db.and_(
                Users.Uname == uname,
                Users.Pwd == pwd
            )
        ).all()
    
    db.session.close()
    status = "invalid"
    if len(users) == 1:
        status = "valid"
    
    # Return the updated value as a JSON response
    return jsonify(stat=status)

@app.route('/register_user', methods=['POST'])
def register_user():
    data = request.json
    uname = data['uname']
    pwd = data['pwd']

    users = Users.query.filter(Users.Uname == uname).all()
    
    status = "invalid"
    if len(uname) == 0:
        status=""
    elif len(users) > 0:
        status = "Username already exists"
    else:
        flag = 0
        status = ""
        if(len(pwd) < 8):
            status += "<br>Requires atleast 8 characters"
            flag = 1
        if not any(char.isupper() for char in pwd):
            status += "<br>Requires atleast one uppercase character"
            flag = 1
        if not any(char.islower() for char in pwd):
            status += "<br>Requires atleast one lowercase character"
            flag = 1
        if not any(is_int(char) for char in pwd):
            status += "<br>Requires atleast one number"
            flag = 1
        if not bool(re.search(r"[!@#$%^&*()-_=+[\]{}|;:'\",.<>/?]", pwd)):
            status += "<br>Requires atleast one special character"
            flag = 1
        if flag == 1:
            status = "Password is weak:"+status
        else:
            try:
                new_user = Users(Uname=uname, Pwd=pwd)
                db.session.add(new_user)
                db.session.flush()       
            except:
                print("Rolling back")
                db.session.rollback()
                db.session.close()
                raise
            else:
                db.session.commit()
                db.session.close()
                print("Commit")
                
            status = "valid" 
    # Return the updated value as a JSON response
    return jsonify(stat=status)

@app.route("/<uname>/manager_dashboard")
def manager_logged_in(uname):
    return render_template("manager_dash.html", user = uname, categories=Category.query.all())

@app.route("/<uname>/user_dashboard")
def user_logged_in(uname):
    return render_template("user_dash.html", user = uname, categories=Category.query.all())
