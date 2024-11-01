from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User 
from werkzeug.security import generate_password_hash, check_password_hash
import random
from datetime import date 
from . import db


auth = Blueprint('auth', __name__) 

def dategen(): 
    today = date.today() 
    return today


def generateUID(): 
    const = "UID" 
    rand =  str(random.randint(1, 10000)) 
    var = const + rand  
    return var





@auth.route('/login', methods = ['GET', 'POST'])
def login(): 
    data = request.form 
    print(data)
    return render_template("login.html", text = "nigga") 


@auth.route('/logout')
def logout(): 
    return "<p>logout</p>"  

@auth.route('/sign_up',  methods = ['GET', 'POST'])
def sign_up(): 
    if request.method == 'POST': 
        firstName = request.form.get('first_name').strip()
        mid = request.form.get('middle_name').strip() 
        lastName = request.form.get('last_name').strip()
        username = request.form.get('username')
        email = request.form.get('email').strip() 
        password = request.form.get('password').strip() 
        password2 = request.form.get("confirm_password").strip() 

        new_User = User( user_id = generateUID(),username = username, doc = dategen(), email_id = email, first_name = firstName, middle_name = mid, last_name = lastName, password = generate_password_hash(password, method='pbkdf2:sha256'))
        db.session.add(new_User)
        db.session.commit() 

        flash('Accoutn created!!' , category = 'success') 
        return redirect(url_for('views.home'))

        
    
    return render_template('sign_up.html')
  




 