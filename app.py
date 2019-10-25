from flask import Flask, render_template, request, session, url_for, redirect, flash

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def root():
    return render_template("index.html", file="time")

@app.route('/<fn>')
def line(fn): 
    return render_template("index.html", file=fn)

@app.route('/data/<file_name>')
def files(file_name):
    with app.open_resource("data/"+file_name) as f:
        contents = f.read()
        return contents

if __name__ == '__main__':
    app.debug = True
    app.run()

