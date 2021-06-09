from flask import Flask, render_template, session, redirect
from functools import wraps

# Setting global language variable, default is English
LANGUAGE = "en"

# Create a Flask Instance
app = Flask(__name__)

def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function



# Create error handlers
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

@app.errorhandler(500)
def page_not_found(e):
	return render_template('500.html'), 500


@app.route('/')
#@login_required	
def index():
	return render_template(f'community-{LANGUAGE}.html')


@app.route('/start')
def start():
	return render_template(f'start-{LANGUAGE}.html')


@app.route('/register')
def register():
	return render_template(f'register-{LANGUAGE}.html')


@app.route('/login')
def login():
	return render_template(f'login-{LANGUAGE}.html')


@app.route('/my_profile')
def my_profile():
	return render_template(f'my_profile-{LANGUAGE}.html')

@app.route('/my_profile/update')
def update_profile():
	return render_template(f'update-{LANGUAGE}.html')


@app.route('/my_profile/settings')
def settings():
	return render_template(f'settings-{LANGUAGE}.html')


@app.route('/messages')
def messages():
	return render_template(f'messages-{LANGUAGE}.html')


@app.route('/logout')
def logout():
	pass


@app.route('/profiles/<id>')
def profiles():
	#return render_template('')
	pass








