from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, \
    EqualTo, Length
from flask_babel import _, lazy_gettext as _l
from app.models import User


class LoginForm(FlaskForm):
    username = StringField(
        _l('Username or Email'), validators=[DataRequired()])
    password = PasswordField(_l('Password'), validators=[DataRequired()])
    remember_me = BooleanField(_l('Remember Me'))
    submit = SubmitField(_l('Sign In'))


class RegistrationForm(FlaskForm):
    username = StringField(_l('Username'), validators=[DataRequired()])
    email = StringField(_l('Email'), validators=[
                        DataRequired(), Email(check_deliverability=True)])
    password = PasswordField(_l('Password'), validators=[
                             DataRequired(), Length(min=8)])
    repeat_password = PasswordField(_l('Repeat password'), validators=[
        DataRequired(),
        EqualTo('password', message=_l('Field must be equal to password.'))])
    submit = SubmitField(_l('Register'))

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError(_('Please use a different username.'))

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError(_('Please use a different email.'))


class ResetPasswordRequestForm(FlaskForm):
    email = StringField(_l('Email'), validators=[
        DataRequired(), Email(check_deliverability=True)])
    submit = SubmitField(_l('Request Password Reset'))


class ResetPasswordForm(FlaskForm):
    password = PasswordField(_l('Password'), validators=[
        DataRequired(), Length(min=8)])
    repeat_password = PasswordField(_l('Repeat password'), validators=[
        DataRequired(), EqualTo('password')])
    submit = SubmitField(_l('Reset Password'))
