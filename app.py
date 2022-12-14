#app.py
from flask import Flask, render_template, flash, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import InputRequired, ValidationError, DataRequired, EqualTo, Length, Email
from wtforms.widgets import TextArea
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import LoginManager, UserMixin, current_user, login_user, logout_user, login_required
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import SubmitField
import time
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

##############################################
#     Creating Posting Functionality         #
##############################################
#Creating a Blog Post Model
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default = datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<post>'.format(self.body)

class PostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    post = TextAreaField('Say something', validators=[DataRequired()])
    submit = SubmitField('Submit')

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

class SearchForm(FlaskForm):
    searched = StringField("Searched", validators=[DataRequired()])
    submit = SubmitField('Submit')

##############################################
#    Creating Following Capability           #
##############################################


# Define the forms in your Flask code
with app.test_request_context():
    follow_form = FlaskForm()
    follow_form.submit = SubmitField('Follow')

    unfollow_form = FlaskForm()
    unfollow_form.submit = SubmitField('Unfollow')


followers = db.Table(
    'followers',
    db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('followed_id', db.Integer, db.ForeignKey('user.id'))
)
# Add this code to the User model
followers = db.relationship(
    'User',
    secondary=followers,
    primaryjoin=(followers.c.follower_id == id),
    secondaryjoin=(followers.c.followed_id == id),
    backref=db.backref('followers', lazy='dynamic'),
    lazy='dynamic'
)
# Add this code to the User model
def follow(self, user):
    if not self.is_following(user):
        self.followed.append(user)

def unfollow(self, user):
    if self.is_following(user):
        self.followed.remove(user)

def is_following(self, user):
    return self.followed.filter(
        followers.c.followed_id == user.id).count() > 0

def followed_posts(self):
    followed = Post.query.join(
        followers, (followers.c.followed_id == Post.user_id)).filter(
            followers.c.follower_id == self.id)
    own = Post.query.filter_by(user_id=self.id)
    return followed.union(own).order_by(Post.timestamp.desc())

#@app.route('/find-users', methods=['GET', 'POST'])
#def find_users():
#    form = SearchForm()
#    if form.validate_on_submit():
#        users = User.query.filter(User.username.like(form.searched.data)).all()
#        return render_template('find-users.html', form=form, users=users, follow_form=follow_form, unfollow_form=unfollow_form)
#    return render_template('find-users.html', form=form, users=None)

# Import the User model from the app module

@app.route('/find-users', methods=['GET', 'POST'])
@login_required
def find_users():
    # Create a form for searching for users
    form = SearchForm()

    # If the form is submitted and the search query is valid
    if form.validate_on_submit():
        # Get the search query from the form
        query = form.searched.data

        # Query the database for users that match the search query
        results = User.query.filter(User.username.like(f"%{query}%")).all()

        # If there are any results, render the search results page and pass the search results to the template
        if results:
            return render_template('search-results.html', results=results)
        # If there are no results, flash a message and redirect to the search page
        else:
            flash("No users found.")
            return redirect(url_for('find_users'))

    # If the form has not been submitted or the search query is invalid, render the search page
    return render_template('find-users.html', form=form)

@app.route('/follow/<username>', methods=['POST'])
def follow_user(username):
    # Get the user with the specified username
    user = User.query.filter_by(username=username).first()

    # If the user exists, add them to the current user's list of followed users
    if user:
        current_user.followed_users.append(user)
        db.session.commit()

        # Return a success response
        return jsonify({'success': True}), 200
    # If the user does not exist, return an error
    else:
        return jsonify({'error': 'User not found'}), 404


@app.route('/unfollow/<username>', methods=['POST'])
def unfollow_user(username):
    # Get the user with the specified username
    user = User.query.filter_by(username=username).first()

    # If the user exists, remove them from the current user's list of followed users
    if user:
        current_user.followed_users.remove(user)
        db.session.commit()

        # Return a success response
        return jsonify({'success': True}), 200
    # If the user does not exist, return an error
    else:
        return jsonify({'error': 'User not found'}), 404

##############################################


#This is our new model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)

    # def __init__(self, username, password):
    #     self.username = username
    #     self.password = password
    
    def is_following(self, other_user):
        # Return True if this user is following the other user, and False otherwise
        pass
    
    def __repr__(self):
        return '<user>'.format(self.username)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def followed_posts(self):
        followed = Post.query.join(
            followers, (followers.c.followed_id == Post.user_id)).filter(
                followers.c.follower_id == self.id)
        own = Post.query.filter_by(user_id=self.id)
        return followed.union(own).order_by(Post.timestamp.desc())

# Old model
# class UserInfo(UserMixin, db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     username = db.Column(db.String(100), unique = True)
#     password = db.Column(db.String(100))
#
#
#
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password



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
        post = Post(title=form.title.data, body=form.post.data, author=current_user)

        form.title.data = ''
        form.post.data = ''

        db.session.add(post)
        db.session.commit()


        flash('Your message is now posted!')
        return redirect(url_for('index'))

    # posts = current_user.followed_posts()
    posts = Post.query.order_by(Post.timestamp.desc());
    page = request.args.get('page', 1, type=int)

    return render_template('index.html', title='Home', form=form, posts=posts)


# Add Post Page
@app.route('/add-post', methods =['GET', 'POST'])
@login_required
def add_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, body=form.post.data, author=current_user)
        # Empty form
        form.title.data = ''
        form.post.data = ''
        # form.author.data = ''

        # Add post to DB
        db.session.add(post)
        db.session.commit()
        # Returns Message
        flash("Post Submitted Successfully!")

    # Redirect to the webpage
    return render_template("add_post.html", form=form)

@app.route('/login', methods=['GET', 'POST'])
def Login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()

            if user is None or not user.check_password(form.password.data):
                flash('Invalid Login Credentials')
                return redirect(url_for('Login'))
            login_user(user)
            return redirect(url_for('index'))
    return render_template('login.html', form = form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method = 'sha256')
        username = form.username.data
        password = hashed_password


        new_register =User(username=username, password=password)

        db.session.add(new_register)

        db.session.commit()

        return redirect(url_for('Login'))


    return render_template('registration.html', form=form)


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

@app.context_processor #to pass stuff to nav bar (via base.html)
def base():
     form = SearchForm()
     return dict(form=form)

@app.route('/search', methods=['POST'])
@login_required
def search():
    form = SearchForm()
    if form.validate_on_submit():
        post_searched = form.searched.data 
        user = User.query.filter_by(username=post_searched).first_or_404()

        return render_template('search.html', form=form, 
        searched=post_searched, user=user)

@app.errorhandler(404)
def page_not_found(error):
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
