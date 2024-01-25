from flask import Flask, render_template
import modules

app = Flask(__name__)
app.register_blueprint(modules.memo_bp)
app.register_blueprint(modules.pomodoro_bp)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)