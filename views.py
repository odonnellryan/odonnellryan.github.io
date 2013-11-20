#this makes the views easy enough to manage. Basically, these templates will be the templates for the
# production site, and the point is to enable us to copy-paste them into where they need to go.

from flask import Flask, Blueprint,render_template

mod = Blueprint('index', __name__)

HOMEPAGE_TITLE = "Test Page Title: "
COMPANY_NAME = "Luma Hosting"

app = Flask(__name__)
app.config.from_object('config')