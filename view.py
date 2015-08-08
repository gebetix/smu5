from flask import Flask, render_template
from flask_bootstrap import Bootstrap


def create_bootstrap_app():
    app = Flask(__name__)
    Bootstrap(app)
    return app


app = create_bootstrap_app()


@app.route('/')
def hello_world():
    return render_template("main.html")


if __name__ == "__main__":
    app.run(debug=True)
