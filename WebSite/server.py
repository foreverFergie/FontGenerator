from flask import Flask,render_template,request

app= Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/')
def img_sub():




if __name__ == "__main__":
    app.run()