from flask import Flask, render_template, url_for

app = Flask(__name__)

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