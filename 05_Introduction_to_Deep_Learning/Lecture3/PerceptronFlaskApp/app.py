from flask import Flask, request

from NeuralNetwork import NeuralNetwork

app = Flask(__name__)
nn = NeuralNetwork()

@app.route('/', methods=['GET'])
def say_hello():
    return "Hello world!"


@app.route('/<name>', methods=['GET'])
def greet_by_name(name):
    return f"Hello {name if name else 'world'}"


@app.route('/in', methods=['GET'])
def get_input_form():
    resp = '<form method="POST" action="/in">'
    resp += '<label for="option1">Has a job?</label>'
    resp += '<input type="radio" id="option1" name="option1" value="yes">Yes</input>'
    resp += '<input type="radio" id="option1" name="option1" value="no">No</input><br>'
    resp += '<label for="option2">Knows Fat Tony?</label>'
    resp += '<input type="radio" id="option2" name="option2" value="yes">Yes</input>'
    resp += '<input type="radio" id="option2" name="option2" value="no">No</input><br>'
    resp += '<label for="option3">Taller than 180cm?</label>'
    resp += '<input type="radio" id="option3" name="option3" value="yes">Yes</input>'
    resp += '<input type="radio" id="option3" name="option3" value="no">No</input><br>'
    resp += '<input type="submit" value="Make prediction">'
    resp += '</form>'
    return resp


@app.route('/in', methods=['POST'])
def post_input_form():
    current_data = [0,0,0]
    current_data[0] = 1 if request.form['option1'] == "yes" else 0
    current_data[1] = 1 if request.form['option2'] == "yes" else 0
    current_data[2] = 1 if request.form['option3'] == "yes" else 0

    prediction = nn.predict(current_data)
    return "Potentially dangerous" if prediction > 0.95 else "Not dangerous"


if __name__ == '__main__':
    app.run()
