#!/usr/bin/env python3
"""
Flask Application with Babel and Locale Selection
This module initializes a Flask web application with internationalization
support using Babel, and selects the best language match for each request.
"""


from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """
    Configuration class for setting up available languages,
    default locale, and timezone.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)


babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    Selects the best match for supported languages based on the request's
    'Accept-Language' headers.
    Returns:
        str: The best matching language code ('en' or 'fr').
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def home():
    """
    Render the home page with a welcoming message.
    Returns:
        Rendered HTML template for the index page.
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
