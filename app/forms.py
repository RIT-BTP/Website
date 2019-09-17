from wtforms import Form, BooleanField, StringField, PasswordField, validators, FileField, TextAreaField
from wtforms.fields.html5 import DateField


class RegistrationForm(Form):
    username = StringField(
        "Username",
        [validators.Length(min=4, max=25)],
        render_kw={"placeholder": "Username"},
    )


class LoginForm(Form):
    username = StringField(
        "Username",
        [validators.Length(min=4, max=25)],
        render_kw={"placeholder": "Username"},
    )
    password = PasswordField("Password", render_kw={"placeholder": "Password"})


class EventForm(Form):
    icon = FileField('Icon')
    name = StringField("Event Name", [validators.Length(min=4, max=25), validators.DataRequired()])
    date = DateField("Event Date")
    description = TextAreaField("Short Description", [validators.Length(min=50, max=500), validators.DataRequired()])
    star = BooleanField("Star")
