from flask import flash
from resto import app
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, redirect, url_for
#from resto import db
from resto.models import user, emp
from resto.models import menu
from resto.forms import menuForm, RegisterForm
from resto import db

# route file


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
# route file


""" @app.route('/food')
def food():
    return render_template('food.html') """


@app.route('/menu')
def menupage():
    menu1 = menu.query.all()
    userquery = user.query.all()
    return render_template('data.html', dishnamesfordisplay=menu1, usersfordisplay=userquery)


@app.route('/add', methods=['GET', 'POST'])
def menuaddpage():
    form = menuForm()
    if form.validate_on_submit():
        dish = menu(dish_name=form.dishname.data,
                    dish_price=form.dishprice.data)
        db.session.add(dish)
        db.session.commit()
    return render_template('cusadd_dish.html', title='New Dish', form=form)


@app.route('/emp')
def employee():
    empnames = emp.query.all()
    print(empnames)
    return render_template('emp.html', empnamesfordisplay=empnames)


# admin page
@app.route('/admin')
def admin():
    return 'this is admin page'


@app.route('/admin/users')
def appuser():
    usernames = user.query.all()
    return render_template('user.html', usernamesfordisplay=usernames)


@app.route('/register', methods=['GET', 'POST'])
def registerpage():
    form = RegisterForm()
    if form.validate_on_submit():
        user1 = user(user_name=form.username.data,
                     user_pass=form.password.data)
        db.session.add(user1)
        db.session.commit()
        # return redirect(url_for(''))
    return render_template('register.html', form=form)


@app.route('/about')
def about():
    return render_template('custabout.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/reserve')
def reserve():
    return render_template('reservation.html')


@app.route('/restmenu')
def restmenupage():
    return render_template('Menu.html')


@app.route('/base')
def base():
    return render_template('base.html')


@app.route('/base/fake')
def fake():
    return render_template('fake.html')


@app.route('/adminbase')
def adminbase():
    return render_template('adminbase.html')


@app.route('/admin/removedish')
def removedish():
    menu1 = menu.query.all()
    return render_template('removedish.html' , toshowdish=menu1 )
