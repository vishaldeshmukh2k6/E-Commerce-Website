from flask import Blueprint, render_template, flash, redirect, url_for
from .forms import LoginForm, SignUpForm
from .models import Customer
from . import db
from flask_login import login_user, logout_user, login_required

auth = Blueprint('auth', __name__)


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    form = SignUpForm()
    if form.validate_on_submit():
        email = form.email.data.strip()
        username = form.username.data.strip()
        password1 = form.password1.data
        password2 = form.password2.data

        if password1 != password2:
            flash('Passwords do not match', 'warning')
            return render_template("signup.html", form=form)
        if Customer.query.filter_by(email=email).first():
            flash('Email already registered!', 'warning')
            return render_template("signup.html", form=form)
        if Customer.query.filter_by(username=username).first():
            flash('Username already taken!', 'warning')
            return render_template("signup.html", form=form)
        try:
            new_customer = Customer(email=email, username=username)
            new_customer.password = password1
            db.session.add(new_customer)
            db.session.commit()
            flash('User created successfully! Please log in.', 'success')
            return redirect(url_for('auth.login'))
        except Exception as e:
            db.session.rollback()
            print("Error creating user:", e)
            flash('Error creating user. Try again later.', 'danger')

    return render_template("signup.html", form=form)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data.strip()
        password = form.password.data
        customer = Customer.query.filter_by(email=email).first()
        print("Customer found:", customer)
        if customer and customer.verify_password(password):
            login_user(customer)
            flash('Logged in successfully!', 'success')
            return redirect(url_for('views.home'))
        elif customer:
            flash('Incorrect password.', 'danger')
        else:
            flash('Email does not exist.', 'warning')
    return render_template("login.html", form=form)


@auth.route('/logout', methods=['GET', 'POST'])
@login_required
def log_out():
    logout_user()
    return redirect('/')

