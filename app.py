from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


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