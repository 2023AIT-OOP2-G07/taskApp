from flask import Flask, render_template, request, redirect, url_for, Blueprint

memo_blueprint = Blueprint("memo", __name__)

# Flaskアプリケーションの作成
app = Flask(__name__)

# メモを格納するリスト
app.config['memos'] = []


@memo_blueprint.route('/')
def index():
    return render_template('memo.html', memos=app.config['memos'])


@memo_blueprint.route('/memo/create_memo', methods=['GET'])
def add_memo():
    return render_template('memo_create_form.html')


if __name__ == '__main__':
    app.run(debug=True)











