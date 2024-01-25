from modules.memo import memo_blueprint
from modules.pomodoro import pomodoro_blueprint

from flask import Flask, render_template
app = Flask(__name__)
app.register_blueprint(memo_blueprint)
app.register_blueprint(pomodoro_blueprint)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
