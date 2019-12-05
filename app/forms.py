from wtforms import (
    Form,
    BooleanField,
    StringField,
    PasswordField,
    validators,
    FileField,
    TextAreaField,
    IntegerField,
)
from wtforms.fields.html5 import DateField, TimeField


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
    icon = FileField("Icon")
    name = StringField(
        "Event Name", [validators.Length(min=4, max=25), validators.DataRequired()]
    )
    date = DateField("Event Date")
    description = TextAreaField(
        "Short Description",
        [validators.Length(min=10, max=500), validators.DataRequired()],
    )
    time = TimeField("Time")
    location = StringField("Location")
    star = BooleanField("Star")


class LeadershipForm(Form):
    icon = FileField("Icon")
    name = StringField(
        "Name", [validators.Length(min=4, max=25), validators.DataRequired()]
    )
    description = TextAreaField(
        "Short Description",
        [validators.Length(min=10, max=500), validators.DataRequired()],
    )
    position = StringField("Position", [validators.DataRequired()])
    major = StringField("Major", [validators.DataRequired()])
    year = IntegerField("Year")


class ManageLeadershipForm(Form):
    active = BooleanField("Active")
