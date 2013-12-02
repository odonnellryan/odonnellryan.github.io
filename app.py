import sys
import os
import views
from forms import user_forms
from flask import Flask, render_template, redirect, url_for, request
from flask_frozen import Freezer
sys.path.append(os.getcwd())

app = Flask(__name__)
app.register_blueprint(views.mod)

app.testing = True
#TODO: turn debugging off
app.debug = True
app.config['FREEZER_DESTINATION'] = 'live'

HOMEPAGE_TITLE = "Test Page Title: "
COMPANY_NAME = "Luma Hosting"

@app.route('/', methods=['GET', 'POST'])
def index():
    register = user_forms.register(request.form)
    content = "Default Page Content"
    return render_template('index.html', content=content, title=HOMEPAGE_TITLE, company_name=COMPANY_NAME, form=register)

@app.route('/cp/', methods=['GET', 'POST'])
def cp():
    register = user_forms.register(request.form)
    content = "Default Page Content"
    return render_template('cp.html', content=content, title=HOMEPAGE_TITLE, company_name=COMPANY_NAME, form=register)

freezer = Freezer(app)
freezer.freeze()

if __name__ == '__main__':
    app.run(port=8000)