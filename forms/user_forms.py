from wtforms import Form, TextField, validators

class register(Form):
    Email = TextField(u'Email', [validators.Length(min=1)])