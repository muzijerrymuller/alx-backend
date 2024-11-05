#!/usr/bin/env python3
"""
Basic Flask Application
This module initializes a Flask web application that renders
a simple 'Hello World' message on the home route.
"""


from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
    """
    Render the home page with a welcoming message.
    Returns:Rendered HTML template for the index page.
    """
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
