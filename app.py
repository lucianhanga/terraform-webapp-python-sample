# flask app which renders a jinj2 template

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # load jinja2 template
    # render template
    return render_template(
        'index.html',
        title= 'Hello World 3'
    ), 200

if __name__ == '__main__':
    app.run()

