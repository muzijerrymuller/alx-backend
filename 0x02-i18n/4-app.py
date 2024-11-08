#!/usr/bin/env python3
"""
Flask Web Application for Internationalization (i18n) Support
------------------------------------------------------------
This is a simple Flask web application that
supports multiple languages using Flask-Babel.
It serves as a foundation for building
multilingual applications by dynamically
selecting the appropriate locale based on the user's request.
Key Features:
-------------
- Configurable language options with default English (en) and French (fr).
- Supports automatic language selection based
on the user's locale preference.
- Renders localized content using the `gettext`
method provided by Flask-Babel.
- Built to handle various HTTP requests and
render content in the selected language.
This application can be extended to support more
languages and localization features,
making it suitable for building internationalized web applications.
"""
from flask import (
    Flask,
    render_template,
    request
)
from flask_babel import Babel


class Config(object):
    """
    Configuration for Babel Localization and Language Preferences
    -------------------------------------------------------------
    This class contains the configuration
    settings for the Flask application
    related to language support and
    timezone settings. It specifies the
    available languages, the default
    language, and the default timezone.
    It is utilized by the Flask app to
    determine how to handle locale-based
    content rendering.
    Attributes:
        LANGUAGES (list): A list of supported languages,
        currently English (en) and French (fr).
        BABEL_DEFAULT_LOCALE (str): The default locale used by
        the application when no locale is specified, set to English ('en').
        BABEL_DEFAULT_TIMEZONE (str): The default timezone
        used by the application, set to UTC.

    """
    LANGUAGES = ["en", "fr"]  # Supported languages: English and French
    BABEL_DEFAULT_LOCALE = "en"  # Default locale (English) if no locale is specified
    BABEL_DEFAULT_TIMEZONE = "UTC"  # Default timezone (UTC) for global consistency


# Initialize Flask application and load configuration
app = Flask(__name__)  # Create the Flask application instance
app.config.from_object(Config)  # Load configuration settings from the Config class
babel = Babel(app)  # Initialize Babel to handle internationalization and localization


@babel.localeselector
def get_locale():
    """
    Determines and Returns the Best Matching Locale for the User
    -----------------------------------------------------------
    This function is called by Flask-Babel
    to determine the appropriate locale
    for the current request. It first checks
    if the user has explicitly provided
    a 'locale' query parameter. If the
    parameter is present and its value matches
    a supported language, it is used.
    Otherwise, the function falls back on the
    browser's accepted languages to find the best matching locale.
    It ensures that the application can
    serve content in the user's preferred
    language, improving the user
    experience for international users.
    Returns:
        str: The locale code (either 'en' for
        English or 'fr' for French), based on
             the user’s request or the browser’s settings.
    """
    loc = request.args.get('locale')
    if loc in app.config['LANGUAGES']:
        return loc
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Renders the Home Page for the Web Application
    ---------------------------------------------
    This route handles HTTP GET requests
    for the application's root URL ('/').
    It is responsible for rendering the home
    page of the application, displaying
    the content in the appropriate language
    based on the user's locale selection.
    By default, this route uses the
    '4-index.html' template, which dynamically
    renders content based on the selected
    language and serves a multilingual user
    interface to improve accessibility for diverse audiences.
    Returns:
        str: The rendered HTML content
        from the '4-index.html' template,
             localized based on the selected locale.
    """
    return render_template('4-index.html')


if __name__ == "__main__":
    """
    Main Entry Point for the Flask Application
    ------------------------------------------
    This block checks if the script is being executed
    directly (not imported as a module).
    It starts the Flask application on port 5000,
    making it accessible to users locally
    or within a network.
    The application is run in debug mode,
    enabling automatic restarts and detailed
    error messages to facilitate development.
    The application listens on all available
    network interfaces (0.0.0.0), which allows
    remote connections from other machines in the same network or container.
    """
    app.run(port="5000", host="0.0.0.0", debug=True)
