from flask import Flask, render_template, url_for, redirect, session, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, length, ValidationError
from flask_bcrypt import Bcrypt
from datetime import timedelta


app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'secrets'
db = SQLAlchemy(app)

app.app_context().push()

default_pass = 'WelcometoBlog123!'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

@app.before_request
def session_handler():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=1)

class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), nullable=False, unique=True)
	password = db.Column(db.String(80), nullable=False)

class LoginForm(FlaskForm):
	username = StringField(validators=[InputRequired(), length(min=4, max=20)], render_kw={"placeholder": "Username"})
	password = PasswordField(validators=[InputRequired(), length(min=4, max=20)], render_kw={"placeholder": "Password"})
	submit = SubmitField("Login")

class SignupForm(FlaskForm):
	username = StringField(validators=[InputRequired(), length(min=4, max=20)], render_kw={"placeholder": "Username"})
	submit = SubmitField("Sign Up")
	
	def validate_username(self, username):
		existing_user_username = User.query.filter_by(
			username=username.data).first()
		
		if existing_user_username:
			raise ValidationError(
				"That username already exists.")

@app.route('/')
def home():
	return render_template('home.html')
	
@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user:
			if bcrypt.check_password_hash(user.password, form.password.data):
				login_user(user)
				return redirect(url_for('dashboard'))
	return render_template('login.html', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
	form = SignupForm()
	
	if form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(default_pass)
		new_user = User(username=form.username.data, password=hashed_password)
		db.session.add(new_user)
		db.session.commit()
		return redirect(url_for('welcome'))
	return render_template('signup.html', form=form)
	
@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
	logout_user()
	return redirect(url_for('login'))

@app.route('/welcome')
def welcome():
	return render_template('welcome.html')

@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
	return render_template('dashboard.html')

if __name__ == '__main__':
	app.run(debug=True)
