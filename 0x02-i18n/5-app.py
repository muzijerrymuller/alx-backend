#!/usr/bin/env python3
"""
Flask Web Application with Mock User Login and Internationalization
-------------------------------------------------------------------
This application demonstrates user login emulation with localization support.
It uses a mock database of users and simulates
logging in by passing a `login_as`
URL parameter. Depending on the user's login status, a personalized greeting
message is displayed in either English or French.
"""
from flask import (
    Flask,
    render_template,
    request,
    g,
    Response
)
from flask_babel import Babel, gettext


class Config(object):
    """
    Configuration for Babel Localization and Language Preferences
    -------------------------------------------------------------
    This class holds the application configuration, specifying supported
    languages and default settings for locale and timezone.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"



users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


def get_user():
    """
    Retrieve a user from the mock database based on `login_as` parameter.
    ---------------------------------------------------------------------
    This function checks if the `login_as`
    parameter is present in the request,
    and if it corresponds to a valid user ID in the mock database (`users`).
    Returns:
        dict or None: A user dictionary if found; otherwise, None.
    """
    try:
        user_id = int(request.args.get('login_as'))
        return users.get(user_id)
    except (TypeError, ValueError):
        return None


@app.before_request
def before_request():
    """
    Set up user context before each request.
    ----------------------------------------
    This function runs before each request, calling `get_user` to check
    if a user is "logged in" based on the `login_as` parameter. If a valid
    user is found, it is set as `g.user` to make it globally available
    within the application.
    """
    g.user = get_user()


@babel.localeselector
def get_locale():
    """
    Determines and Returns the Appropriate Locale for the Request
    -------------------------------------------------------------
    This function checks the `locale` query parameter and verifies if the
    requested language is supported. If not specified or unsupported,
    it defaults to the browser’s preferred language.
    Returns:
        str: The language code (e.g., 'en' or 'fr') selected for localization.
    """
    loc = request.args.get('locale')
    if loc in app.config['LANGUAGES']:
        return loc
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> Response:
    """
    Home Page Route
    ---------------
    Renders the home page with a localized greeting message based on
    the user's login status. Sets response to UTF-8 encoding.
    Returns:
        Response: Rendered HTML content of the home page with either a
                  personalized greeting or a
                  default message, with UTF-8 encoding.
    """
    if g.user:
        greeting = gettext("You are logged in as %(username)s.", username=g.user['name'])
    else:
        greeting = gettext("You are not logged in.")
    rendered_content = render_template('5-index.html', greeting=greeting)
    response = Response(rendered_content)
    response.headers["Content-Type"] = "text/html; charset=utf-8"
    return response


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)
