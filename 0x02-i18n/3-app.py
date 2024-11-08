#!/usr/bin/env python3
"""A Basic Flask Web Application with Internationalization Support.
This script initializes a simple Flask application that incorporates
internationalization (i18n) features via Flask-Babel. The application is
configured to support multiple languages, enabling users to view the web
pages in either English or French based on their
preferences. The configuration
is structured to promote seamless adaptability
for additional languages, timezone
handling, and robust locale management.
Modules:
    flask_babel: Provides the Babel extension for i18n support within Flask.
    flask: The core Flask framework used to create the web application.
"""

from flask_babel import Babel
from flask import Flask, render_template, request


class Config:
    """Configuration class for Flask-Babel settings.
    This class encapsulates essential configurations required by Flask-Babel,
    such as supported languages, the default language locale,
    and the timezone.
    Designed to be modular and easily extensible, these settings serve as the
    backbone of the application’s localization functionality, allowing for
    seamless language switching and timezone management.
    Attributes:
    LANGUAGES (list): Specifies the supported languages for the application.
    BABEL_DEFAULT_LOCALE (str): Sets the default language
    (locale) for the app.
        BABEL_DEFAULT_TIMEZONE (str): Defines the default timezone for Babel.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Determines the best-matching language locale for the user.
    This function leverages Flask-Babel’s `localeselector` decorator to
    dynamically determine the language locale for each request. It matches
    the user's language preferences from the browser's headers with the
    application's supported languages, providing a personalized experience.
    Returns:
        str: The best-matching language code (e.g., 'en' or 'fr'), based on
        user preferences or the application default.
    """
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def get_index() -> str:
    """Renders the homepage of the web application.
    The function serves as the view for the application's root endpoint,
    rendering the `3-index.html` template. This page is dynamically
    localized based on the determined locale, enabling users to view
    content in their preferred language.
    Returns:
        str: Rendered HTML content for the homepage, adjusted for localization.
    """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
