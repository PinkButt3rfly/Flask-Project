from flask import Flask, render_template, request
import json

app = Flask(__name__)

notes = []

@app.route('/')
def index():
    load_notes()
    return render_template('index.html', notes=notes)

def load_notes():
    global notes
    try:
        with open('notes.json', 'r') as file:
            notes = json.load(file)
    except FileNotFoundError:
        notes = []

if __name__ == '__main__':
    app.run(debug=True)




#@app.route('/news')
#def new():
#if (request.method == 'GET'):
#    return '<h1>Hi this is our news page with GET'
#else:
#    return "<p>Hello, World, Greatest1!!!!</p>"