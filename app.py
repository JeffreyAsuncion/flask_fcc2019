from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)


# Set up data base 
#.. This will replace the hard coded "all_posts"
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(30), nullable=False, default='Author Unknown...')
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return 'Blog post ' + str(self.id) 

#dummy data ie from database
all_posts = [
    {
        'title': 'Post 1',
        'content': 'In the light of the moon a little egg lay on a leaf. Isabelley, Isabelley',
        'author': 'Isabella Grace'
    },
    {
        'title': 'Post 2',
        'content': 'One Sunday morning the warm sun cam up... Night and Day Isabelley'
    }

]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/posts')
def posts():
    return render_template('posts.html', posts=all_posts)


# use this to get input from url
@app.route('/home/users/<string:name>/posts/<int:id>')
def hello(name, id):
    return "Hello, " + name + " Your id is :" + str(id)

# use to onlyget
@app.route('/onlyget', methods=['GET', 'POST'])
def get_req():
    return 'You can only get this webpage. 4'


if __name__ == "__main__":
    app.run(debug=True)