from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = "secretKey"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninjas/<ninja_color>')
def color(ninja_color):
    return render_template('ninjas.html', color=ninja_color, tmnt=False)




app.run(debug=True)
