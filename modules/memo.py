from flask import Flask, render_template, request, redirect, url_for, Blueprint

memo_blueprint = Blueprint("memo", __name__)

# Flaskアプリケーションの作成
app = Flask(__name__)

# メモを格納するリスト
app.config['memos'] = []


@memo_blueprint.route('/')
def index():
    return render_template('memo.html', memos=app.config['memos'])


@memo_blueprint.route('/add_memo', methods=['POST'])
def add_memo():
    # フォームからのデータを取得
    new_memo = request.form.get('memo_text')

    # メモを追加
    app.config['memos'].append(new_memo)

    # メモ一覧ページにリダイレクト
    return redirect(url_for('memo.index'))

# BlueprintをFlaskアプリケーションに登録
app.register_blueprint(memo_blueprint)


if __name__ == '__main__':
    app.run(debug=True)











