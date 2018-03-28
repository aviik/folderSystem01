from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from helloWorld import *




app=Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)
