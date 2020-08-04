from flask import Flask
from flask import render_template, request, redirect
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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/posts', methods=['GET', 'POST'])
def posts():

    if request.method == 'POST':
        post_title = request.form['title']
        post_content = request.form['content']
        post_author = request.form['author']
        new_post = BlogPost(title=post_title, content=post_content, author=post_author)
        db.session.add(new_post)
        db.session.commit()
        return redirect('/posts')
    else:
        all_posts = BlogPost.query.order_by(BlogPost.date_posted).all()
        return render_template('posts.html', posts=all_posts)


# # use this to get input from url
# @app.route('/home/users/<string:name>/posts/<int:id>')
# def hello(name, id):
#     return "Hello, " + name + " Your id is :" + str(id)

# # use to onlyget
# @app.route('/onlyget', methods=['GET', 'POST'])
# def get_req():
#     return 'You can only get this webpage. 4'


@app.route('/posts/delete/<int:id>')
def delete(id):
    post = BlogPost.query.get_of_404()
    db.session.delete(post)
    db.session.commit()
    return redirect('/posts')

@app.route('/posts/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):

    post = BlogPost.query.get_or_404(id)

    if request.method == 'POST':
        
        post.title = request.form['title']
        post.author = request.form['aannple']
        post.title = request.form['title']
        db.session.commit()
        return redirect('/edit.html')
    else:
        return render_template('edit.html', post=post)


if __name__ == "__main__":
    app.run(debug=True)