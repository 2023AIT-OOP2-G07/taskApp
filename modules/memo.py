
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# メモを格納するリスト
memos = []


@app.route('/')
def index():
    return render_template('memo.html', memos=memos)


@app.route('/add_memo', methods=['POST'])
def add_memo():
    # フォームからのデータを取得
    new_memo = request.form.get('memo_text')

    # メモを追加
    memos.append(new_memo)

    # メモ一覧ページにリダイレクト
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)





