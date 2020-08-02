from flask import Flask

app = Flask(__name__)

# use this to get input from url
@app.route('/home/users/<string:name>/posts/<int:id>')
def hello(name, id):
    return "Hello, " + name + " Your id is :" + str(id)

# use to onlyget
@app.route('/onlyget', methods=['GET', 'POST'])
def get_req():
    return 'You can only get this webpage.'


if __name__ == "__main__":
    app.run(debug=True)