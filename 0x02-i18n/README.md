0. Basic Flask App Setup
You’ll learn how to set up a simple Flask application by:

Creating a basic route ("/") and linking it to an HTML template.
Creating a simple HTML template that displays specific content in the
This will introduce you to the fundamentals of Flask routing and the basics of working with HTML templates in Flask.

1. Basic Babel Setup
By installing and configuring Babel, you’ll understand:

How to set up Flask-Babel, a Flask extension for internationalization (i18n) and localization (L10n).
Defining configurations like available languages and default settings for locale and timezone through a Config class.
This step shows you how to make your Flask app multilingual and timezone-aware, laying the foundation for more complex internationalization.

2. Get Locale from Request
Creating the get_locale function will teach you:

How to use Flask-Babel’s @babel.localeselector decorator to dynamically select a user’s preferred language based on their request headers.
This function helps you create a user-centered application that adapts content language based on user preferences automatically detected from their browser settings.

3. Parametrize Templates
In this part, you’ll learn how to:

Use the _ (gettext) function to translate text within templates.
Set up babel.cfg and extract translation strings into a .pot file.
Initialize translation dictionaries and define translations in messages.po files for English and French.
This process introduces you to the workflow of defining and managing translations, a key aspect of creating applications that serve content in multiple languages.

4. Force Locale with URL Parameter
Here, you’ll add functionality to override language selection through URL parameters, teaching you:

How to check URL parameters for specific values and override defaults based on those values.
This step is useful for testing and demonstrates how users can explicitly request a particular language, enhancing flexibility.

5. Mock Logging In
By creating a mock user login system, you’ll learn:

How to create a mock user table and retrieve user information based on URL parameters.
Using @app.before_request to set up actions that run before each request, such as checking for logged-in users and storing their information in flask.g.
This demonstrates how to use flask.g to store global data for the duration of a request, which is useful for managing user-specific settings.

6. Use User Locale
Enhancing the get_locale function shows you:

How to prioritize different sources (URL, user settings, request headers, defaults) for language selection.
This step teaches you about handling multiple sources of data for configuration, which is essential when creating adaptable applications.

7. Infer Appropriate Time Zone
Finally, you’ll create a get_timezone function, gaining insights into:

The @babel.timezoneselector decorator for selecting a timezone.
Validating and setting timezones using the pytz library to ensure compatibility with various time zones.
This will help you understand timezone management, especially with global users, and prepare you for real-world applications where timezone accuracy is crucial.
