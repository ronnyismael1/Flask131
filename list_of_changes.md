# Flask131

File changes
-added some imports
-changed imports into one line
-deleted forms file and moved it in app.py
-added functionality to prompt user to use a different username if username is already registered
-added class Post 
-added class PostForm
-added GET POST methods for /login route
-removed __init__ methods with __repr__ methods
-updated route(‘/) and route(‘/index’)
-updated route(‘/login) and route(‘/register)
-added formhelpers.html
-added post.html
-updated base.html with new “container” class

Variable name changes
-class UserInfo() -> User()
-(in User class) password -> password_hash

Functionality
-added functionality to post and view own posts on home page
-added functionality of clickable profile (shows last seen, and posted messages)
