from web_app import db
from flask import Blueprint
from web_app .models import User
from .forms import RegisterForm, LoginForm
from flask import render_template, url_for, flash, redirect
from flask_login import login_user, logout_user, login_required


auth = Blueprint('auth', __name__)


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()  # this is to call the instance of the the register form
    if form.validate_on_submit():
        user = User(username=form.username.data, email_address=form.email_address.data, password=form.password1.data)  # this is taken the agument from password hash from model
        db.session.add(user)
        db.session.commit()
        flash(f'Account created successfully! {user.username} You can now login', category='success')
        return redirect(url_for('auth.login'))
    if form.errors != {}:  # if there are not errors from the validations
        for err_msg in form.errors.values():  # fetching the value from dic values
            flash(f'Registration unsuccessful: {err_msg}', category='danger')
    return render_template('signup.html', form=form)



@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()  
    if form.validate_on_submit():  
        user = User.query.filter_by(email_address=form.email_address.data).first()
        if user and user.check_password_correction(attempted_password=form.password.data):
            login_user(user, remember=form.remember.data)
            flash(f'Success! You are logged in as {user.email_address}', category='success')
            return redirect(url_for('main_page.main'))
        else:
            flash('Login Unsuccessful! Please check email address and password',category='danger')
    return render_template('login.html', form=form)



@auth.route('/logout')  
def logout():
    logout_user()
    flash('You have been loged out successfully', category='success')
    return render_template('home.html') 
