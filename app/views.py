from flask import render_template, Blueprint, request, redirect, url_for, flash

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')