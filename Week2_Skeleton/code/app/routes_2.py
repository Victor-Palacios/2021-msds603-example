from app import application
from flask import render_template, redirect, url_for
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import SubmitField
import os


class UploadFileForm(FlaskForm):
    """Class for uploading file when submitted"""


def index():
    """Index Page : Renders index.html with author name."""
    return (render_template('index.html', author='Diane Woodbridge'))


@application.route('/upload', methods=['GET', 'POST'])
def upload():
