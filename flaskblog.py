import flask
from flask import Flask

#This is some dummy data that will be used to simulate post entries
dummy_posts = [
    {
        'title': 'posting 1',
        'author': 'maLo',
        'date_posted': 'Jan. 17th, 2021',
        'content': "I am the best"
    },

    {
        'title': 'posting 2',
        'author': 'miLi',
        'date_posted': 'Jan. 17th, 2021',
        'content': "Nonsense"
    }
]


# The argument passed to the Flask constructor tells Flask where to
# look for templates and static files
app = Flask(__name__)

# Decorator to return the content of each page
@app.route("/")
def home_page():
    # Any keyword argument added to flask.render_template can be used on the html content
    # Check out each html file to see the syntax supported by the render_template engine
    return flask.render_template('home.html', data=dummy_posts)

@app.route("/about")
def about_page():
    return flask.render_template('about.html', title='About')

# This runs Flask directly when runnin the Python file
#   debug=True let us see the changes made to the Python files immediately when refreshing the page
#   otherwise we would have to set some environment variables and setting the debug mode when executing
#   Flask from the console.
if __name__ == '__main__':
    app.run(debug=True)