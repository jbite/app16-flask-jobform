from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/submit", methods=["POST"])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        print(name, email, message)
        return redirect(url_for('success'))

@app.route('/success')
def success():
    return 'Form submitted successfully'

app.run(debug=True, port=5001)

