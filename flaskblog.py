from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

# Key only used for demo app. Make environment variable.
app.config['SECRET_KEY'] = '77e6105f44f7aab694bd4aba5fca021d'

posts = [
    {
        'author' : 'Samuel Nelson',
        'title' : 'Blog Post 1',
        'content' : 'first post content',
        'date_posted' : '01-23-1987'
    },
    {
        'author' : 'John Doe',
        'title' : 'Blog Post 2',
        'content' : 'second post content',
        'date_posted' : '01-12-1387'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='about')


if __name__ == '__main__':
    app.run(debug=True)