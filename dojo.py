from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    print "Got Post Info"
    print request.form



    return render_template('result.html')

app.run(debug=True)
