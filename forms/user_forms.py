from wtforms import Form, PasswordField, TextField, validators

class register(Form):
    Email = TextField(u'Username', [validators.Length(min=1)])
    Password = PasswordField(u'Password', [validators.Length(min=1)])