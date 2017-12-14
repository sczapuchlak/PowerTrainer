from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email, Length
#http://wtforms.simplecodes.com/docs/1.0.1/crash_course.html HELPED IMMENSELY
# flask forms
class LoginForm(FlaskForm):
    username = StringField('Username:', validators=[InputRequired(), Length(min=3, max=50)])
    password = PasswordField('Password:', validators=[InputRequired(), Length(min=6, max=100)])



class SignupForm(FlaskForm):
    username = StringField('Username:', validators=[InputRequired(), Length(min=3, max=50)])
    password = PasswordField('Password:', validators=[InputRequired(), Length(min=6, max=100)])
    email = StringField('Email:', validators=[InputRequired(), Email(), Length(min=8, max=50)])
    submit = SubmitField("Sign In")


class ExerciseForm(FlaskForm):
    exercise = StringField('Exercise Name:', validators=[InputRequired(), Length(min=3, max=50)])
    weight = StringField('Weight Amount:', validators=[InputRequired(), Length(min=3, max=50)])
    repetition = StringField('Repetition:', validators=[InputRequired(), Length(min=3, max=50)])