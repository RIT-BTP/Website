from wtforms import Form, BooleanField, StringField, PasswordField, validators


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
    password = PasswordField(
        "Password",
        render_kw={"placeholder": "Password"},
    )