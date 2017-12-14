import Models
from Forms import SignupForm, LoginForm, ExerciseForm
from flask import Flask, render_template, request, redirect, session, flash
from flask_login import login_user, logout_user, LoginManager, login_required

# set up the application with Flask
app = Flask(__name__, '/static', static_folder='static', template_folder='templates')
app.debug = True
# this is so the templates always reload when there are changes made
app.config['TEMPLATES_AUTO_RELOAD'] = True
# # create the table

# dbdb.createDBandTable()
app.secret_key = 'noone can guess this'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/powertrainer.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# login manager handles login validation and current logged in user
login_manager = LoginManager()
login_manager.init_app(app)

# establish and create database
def init_db():
    Models.database.init_app(app)
    Models.database.app = app
    Models.database.create_all()

@login_manager.user_loader
def load_user(username):
    return Models.User.query.filter_by(username=username).first()


def load_user_id(user_id):
    return Models.User.query.filter_by(user_id=user_id).first()


# display the homepage
@app.route('/')
@app.route('/index.html')
@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/signup.html', methods=['GET'])
def signup():
    return render_template('signup.html', form=SignupForm())

@app.route('/login.html', methods=['GET'])
def login():
    return render_template('login.html', form=LoginForm())

@app.route('/userHome.html', methods=['GET'])
def userHome():
    return render_template('userHome.html',form=ExerciseForm())


@app.route('/newEntry', methods=['POST'])
# this will add the exercises in the database
def createEntry():
    exercise_form = ExerciseForm()

    if request.method == 'GET':
        return render_template('userHome.html', form=exercise_form)

    elif request.method == 'POST':

        if exercise_form.validate_on_submit():

                # create new exercise
                new_exercise = Models.Exercise(exercise_form.exercise.data, exercise_form.weight.data,
                                               exercise_form.repetition.data)
                Models.database.session.add(new_exercise)
                Models.database.session.commit()
                return render_template('userHome.html', userEntry=new_exercise,form=exercise_form  )

@app.route('/register', methods=['POST'])
# this will display the sign up page and let you sign up
def register():
    # setting up flask form
    register_form = SignupForm()

    if request.method == 'GET':
        return render_template('signup.html', form=register_form)

    elif request.method == 'POST':

        if register_form.validate_on_submit():
            if Models.database.session.query(Models.User).filter_by(username=register_form.username.data).first():
                return "User already exists"
            else:
                # create new user
                new_user = Models.User(register_form.username.data, register_form.password.data,
                                       register_form.email.data)
                Models.database.session.add(new_user)
                Models.database.session.commit()
                session['username'] = new_user.username
                login_user(new_user)


                # adding user to session

                flash('User Created')
                return redirect("userHome.html")
        else:
            return "Form didn't validate"


@app.route('/signin', methods=['POST'])
# this will allow the user to signin
def signin():
    login_form = LoginForm()

    if request.method == 'GET':
        return render_template('login.html', form=login_form)

    # login form
    elif request.method == 'POST':

        if login_form.validate_on_submit():

            user = Models.User.query.filter_by(username=login_form.username.data).first()

            if user:
                if user.password == login_form.password.data:
                    login_user(user)
                    session['username'] = user.username
                    return redirect('userHome.html')
                else:
                    return "Incorrect Password or Username"
            else:
                return "User doesn't exist"
        else:
            return "form not validated"




@app.route('/testimonials.html', methods=['GET'])
# this will display the cart
def testimonials():
    return render_template('testimonials.html')

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('logout.html')
# @app.route("/signout", methods=['POST', 'GET'])
# def signout():
#     '''sign the current user out'''
#     sign_user_out()
#     return redirect('/')
#
# def sign_user_out():
#     '''remove the information from the session to sign a user out'''
#     del session['username']
#     del session['expiration']
#     logout_user()

if __name__ == '__main__':
    init_db()
    app.run()
