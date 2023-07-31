from flask import Flask
from flask import render_template
from flask import request, jsonify
import models

app = Flask(__name__)
UPLOAD_FOLDER = 'static/images/'

app = Flask(__name__)

@app. route("/")
def home():
    return render_template("home.html")

@app. route("/login")
def login_page():
    return render_template("login.html")

@app.route('/update', methods=['POST'])
def update_value():
    data = request.json
    uname = data['uname']
    pwd = data['pwd']
    
    # Return the updated value as a JSON response
    return jsonify(updated_value=value)
    
if __name__ == "__main__":
    app. debug=True
    app.run()
