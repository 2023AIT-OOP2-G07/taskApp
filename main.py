from modules.memo import memo_bp
from flask import Flask, render_template
app = Flask(__name__)
app.register_blueprint(memo_bp)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
