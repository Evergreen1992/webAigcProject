from flask import Flask, render_template
from flask import request

app = Flask(import_name="")

@app.route('/')
def home(name=None):
    return render_template("index.html", name=name)

if __name__ == '__main__':
    print("...start server...")
    app.run(host='0.0.0.0', port=8080)