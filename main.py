from flask import Flask, render_template
from modules import memo_bp, pomodoro_bp, todo_bp

app = Flask(__name__)
app.register_blueprint(memo_bp)
app.register_blueprint(pomodoro_bp)
app.register_blueprint(todo_bp)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)