from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///friends_post.db'
app.config['SECRET_KEY'] = '3af0739eb8aaaa294356e5e9'


db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager .login_view = 'auth.login'
login_manager .login_message_category = 'info'


from web_app.auth.routes import auth
from web_app.main.routes import main_page
from web_app.posts.routes import posts
from web_app.views.routes import views
from web_app.account.routes import accounts
from web_app.errors.handlers import errors


app.register_blueprint(auth, url_prefix='/')
app.register_blueprint(main_page, url_prefix='/')
app.register_blueprint(posts, url_prefix='/')
app.register_blueprint(views, url_prefix='/')
app.register_blueprint(accounts, url_prefix='/')
app.register_blueprint(errors, url_prefix='/')