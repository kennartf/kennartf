from flask import Blueprint
from flask import render_template


views = Blueprint('views', __name__)


@views.route('/')
@views.route('/home')
def home():
    return render_template('home.html')
    

@views.route('/about') 
def about():
    return render_template('about.html')  


@views.route('/contact') 
def contact():
    return render_template('contact.html')  
