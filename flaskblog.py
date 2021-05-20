import flask
from flask import Flask

# The argument passed to the Flask constructor tells Flask where to
# look for templates and static files
app = Flask(__name__)

# Decorator to return the content of each page
@app.route("/")
def home_page():
    return flask.render_template('home.html')

@app.route("/about")
def about_page():
    return flask.render_template('about.html')

# This runs Flask directly when runnin the Python file
#   debug=True let us see the changes made to the Python files immediately when refreshing the page
#   otherwise we would have to set some environment variables and setting the debug mode when executing
#   Flask from the console.
if __name__ == '__main__':
    app.run(debug=True)