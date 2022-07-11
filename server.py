from flask import Flask, render_template, request, session , redirect
app = Flask(__name__)

app.secret_key = 'yadabobbbaba'

@app.route('/')
def index():
    session.clear()
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['favlang'] = request.form.getlist('favlang')
    # session['favlang1'] = request.form['favlang1']
    # session['favlang2'] = request.form['favlang2']
    # session['favlang3'] = request.form['favlang3']
    # session['favlang4'] = request.form['favlang4']
    # session['favlang5'] = request.form['favlang5']
    session['comments'] = request.form['comments']
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('result.html')


if __name__=="__main__": 
    app.run(debug=True,port=5001)

# http://localhost:5000 - have this display a nice looking HTML form.  The form should be submitted to '/process'
# Save form data into session.
# http://localhost:5000/result - have this display a html with the information that was submitted by POST