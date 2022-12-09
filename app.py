#app.py
from flask import Flask, render_template, flash, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import LoginManager, UserMixin, current_user, login_user, logout_user, login_required
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import InputRequired, ValidationError, DataRequired, EqualTo, Length, Email

import os

#create the object of Flask
app  = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config.update(
    SECRET_KEY='this-is-a-secret',
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db'),
    SQLALCHEMY_TRACK_MODIFICATIONS = False
)

#login code
login_manager = LoginManager()
login_manager .init_app(app)
login_manager .login_view = 'Login'

db = SQLAlchemy(app)

@app.before_first_request
def create_tables():
    db.create_all()

followers = db.Table(
    'followers',
    db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('followed_id', db.Integer, db.ForeignKey('user.id'))
)

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password_hash = db.Column(db.String(100))
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)

    # def __init__(self, username, password):
    #     self.username = username
    #     self.password = password

    def __repr__(self):
        return '<user>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def followed_posts(self):
        followed = Post.query.join(
            followers, (followers.c.followed_id == Post.user_id)).filter(
                followers.c.follower_id == self.id)
        own = Post.query.filter_by(user_id=self.id)
        return followed.union(own).order_by(Post.timestamp.desc())

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<post>'.format(self.body)

class PostForm(FlaskForm):
    post = TextAreaField('Say something', validators=[DataRequired()])
    submit = SubmitField('Submit')


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():

    form = PostForm()
    if form.validate_on_submit():
        post = Post(body=form.post.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your message is now posted!')
        return redirect(url_for('index'))

    posts = current_user.followed_posts().all()
    page = request.args.get('page', 1, type=int)

    return render_template('index.html', title='Home', form=form, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def Login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid Credentials')
            return redirect(url_for('Login'))
        login_user(user)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Success, You are now registered!')
        return redirect(url_for('Login'))
    return render_template('registration.html', title='Register', form=form)

@app.route('/delete/<username>')
@login_required
def delete(username):
    if(username == current_user.username):
        delete_user = User.query.first_or_404(username)

        try:
            db.session.delete(delete_user)
            db.session.commit()
            flash('Success, User has been deleted!')
            logout_user()
            return redirect(url_for('index'))
        except:
            flash('Error, could not delete user')
    else:
        flash('You can not delete that user')
        return redirect(url_for('user', username=current_user.username))

@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    page = request.args.get('page', 1, type=int)
    posts = current_user.followed_posts().all()

    return render_template('user.html', user=user, posts=posts, username=username)

if __name__ == '__main__':
    app.run(debug=True)
