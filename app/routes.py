from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')

def index(): 
    user = {"username": "Jackson"}

    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

# just instantiating the login page, route.py seems like our main file
# for routing all the pages into one. 
@app.route('/login', methods=['GET', 'POST']) # decorateive, telling to accept GET and POST requests
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login request for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url._for(index))
    return render_template('login.html', title="Sign In", form=form)