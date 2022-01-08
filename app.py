from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/registration')
def registration():
    return render_template("registration.html")

@app.route('/autorize')
def autorize():
    return render_template("index_autorize.html")

@app.route('/elect')
def elect():
    return render_template("elect.html")

@app.route('/techinck')
def techinck():
    return render_template("techinck.html")

@app.route('/clothes')
def clothes():
    return render_template("clothes.html")

@app.route('/verify', methods = ['POST', 'GET'])
def registration_verify():
    if request.method == 'POST':
        return redirect("/registration")

@app.route('/verify', methods = ['POST', 'GET'])
def autorize_verify():
    if request.method == 'POST':
        return redirect("/index_autorize")

@app.route('/verify', methods = ['POST', 'GET'])
def elect_verify():
    if request.method == 'POST':
        return redirect("/elect")

@app.route('/verify', methods = ['POST', 'GET'])
def techinck_verify():
    if request.method == 'POST':
        return redirect("/techinck")

@app.route('/verify', methods = ['POST', 'GET'])
def clothes_verify():
    if request.method == 'POST':
        return redirect("/clothes")



if __name__ == "__main__":
    app.run()
