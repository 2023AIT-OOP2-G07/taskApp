from modules.memo import memo_blueprint
from flask import Flask
app = Flask(__name__)
app.register_blueprint(memo_blueprint)

if __name__ == '__main__':
    try:
        app.run(debug=True)
    except Exception as e:
        print(f"An error occurred: {e}")
