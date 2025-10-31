from flask import Blueprint, render_template, flash, redirect, url_for
from .forms import LoginForm, SignUpForm
from .models import Customer
from . import db
from flask_login import login_user, logout_user, login_required

auth = Blueprint('auth', __name__)


@auth.route('/sign-up' , methods=['GET', 'POST'])
def sign_up():
    form = SignUpForm()
    if form.validate_on_submit():
        email = form.email.data
        username = form.username.data
        password1 = form.password1.data
        password2 = form.password2.data

        if password1 == password2:
            new_customer = Customer
            new_customer.email = email
            new_customer.username = username
            new_customer.password = password2

            try:
                db.session.add(new_customer)
                db.session.commit()
                flash('User Created Successfully')
                return redirect('/login')
            except Exception as e:
                print('Error creating user: ' + str(e))
                flash('Error creating user')

            form.email.data = ''
            form.username.data = ''
            form.password1.data = ''
            form.password2.data = ''   


    return render_template("signup.html", form=form)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        customer = Customer.query.filter_by(email=email).first()

        if customer:
            if customer.verify_password(password):
                flash('Logged in successfully')
                login_user(customer)
                return redirect('/')
            else:
                flash('Incorrect password')
        else:
            flash('Email does not exist') 

    return render_template("login.html", form=form)


@auth.route('/logout', methods=['GET', 'POST'])
@login_required
def log_out():
    logout_user()
    return redirect('/')

