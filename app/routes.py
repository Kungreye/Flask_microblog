from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Kungreye'}
    posts = [
        {
            'author': {'username': 'Tsui'},
            'body': 'This issue is getting on my nerves!'
        },
        {
            'author': {'username': 'Feng'},
            'body': 'Apologize, man. Really sorry for that.'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))   # url_for(view_function_name) for URL(attached to the view_function)
    return render_template('login.html', title='Sign In', form=form)