from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# メモのリスト
memos = []

@app.route('/')
def index():
    return render_template('index.html', memos=memos)

@app.route('/add_memo', methods=['POST'])
def add_memo():
    memo_content = request.form.get('memo_content')
    if memo_content:
        memos.append(memo_content)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)



