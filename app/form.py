from flask_wtf import Form
from wtforms import TextField, PasswordField, SelectField,validators
from wtforms.validators import InputRequired
from model import Profile
#implement later->from model import Profile

class CreateProfileForm(Form):
    firstname = TextField('Firstname',validators=[InputRequired()])
    lastname = TextField('Lastname', validators=[InputRequired()])
    username = TextField('Username', validators=[InputRequired()])
    bio = TextField('Biography', validators=[InputRequired()])
    gender = SelectField(u'Gender', choices=[('Male', 'Male'),('Female','Female')])
    age = TextField('Age',validators =[InputRequired()])
    password = PasswordField('New Password',[validators.DataRequired(),
                                             validators.EqualTo('confirm', message='Passwords dont match')])
    confirm=PasswordField('Confirm Password')

 
class LoginForm(Form):
    username = TextField('Username', [validators.Required()])
    password = PasswordField('Password', [validators.Required()])

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.user = None

    def validate(self):
        rv = Form.validate(self)
        if not rv:
            return False

        profile = Profile.query.filter_by(
            username=self.username.data).first()
        if user is None:
            self.username.errors.append('Unknown username')
            return False

        if not user.check_password(self.password.data):
            self.password.errors.append('Invalid password')
            return False

        self.user = user
        return True
    
