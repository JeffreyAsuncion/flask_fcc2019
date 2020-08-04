# flask_fcc2019
Learn Flask for Python - Full Course in 3 hours
Clever Programmer

2020.08.01 timestamp 0:21:48
2020.08.02 timestamp 0:38:53
2020.08.02 timestamp 0:48:49
after db is created in app.py
terminal>python>from app import db
>>>db.create_all()
>>>terminal>python>from app import BlogPost
>>>BlogPost.query.all()
[] nothing in db now
>>>db.session.add(BlogPost(title='Blog Post 1', content='In the light of the moon a little egg lay on a leaf.', author='Isabelley'))
>>>db.session.add(BlogPost(title='Blog Post 2', content='One Sunday morning the warm sun came up...', author='Owl'))
>>>BlogPost.query.all()
[Blog post 1, Blog post 2]
>>> BlogPost.query.all()[0].author
'Isabelley'
>>> BlogPost.query.all()[1].content
'One Sunday morning the warm sun came up...'
>>> BlogPost.query.all()[1].date_posted
datetime.datetime(2020, 8, 2, 19, 15, 38, 857502)

timestamp 1:14:58 front end inputs
timestamp 1:23:05 back end working