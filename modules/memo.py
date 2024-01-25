from crypt import methods
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, Blueprint
import json

memo_blueprint = Blueprint("memo", __name__)

# Flaskアプリケーションの作成
app = Flask(__name__)

# メモを格納するリスト
# Example:
#     app.config['memo_dict']: dict = {
#         '20220101120000': {'title': 'Meeting', 'body': 'Prepare presentation'},
#         '20220102153000': {'title': 'Shopping List', 'body': 'Milk, Eggs, Bread'}
#     }
MEMO_FILE = "./static/data/memo_data.json"
app.config['memo_dict']: dict[str, {str, str}] = {}


@memo_blueprint.route('/memo')
def index():
    app.config['memo_dict'] = json.load(open(MEMO_FILE, 'r', encoding='utf-8'))
    return render_template('memo.html', memo_dict=app.config['memo_dict'])


@memo_blueprint.route('/memo/add', methods=['POST'])
def add_memo():
    """
    メモを追加するためのルート。メモリストにメモを追加するPOSTリクエストを処理します。
    パラメーター: なし
    戻り値: メモページへのリダイレクト
    """
    save = request.form.get('memo_save', None)
    # delete = request.form.get('memo_delete', None) # 実装する時に追加してください

    if save is not None:
        title = request.form.get('memo_title', '')
        body = request.form.get('memo_body', '')

        key = request.form.get('memo_key', '')
        if key == '':
            key = datetime.now().strftime("%Y%m%d%H%M%S%f")
            app.config['memo_dict'].update(
                {key: {'title': title, 'body': body}})
        else:
            app.config['memo_dict'][key]['body'] = body

        json.dump(app.config['memo_dict'], open(
            MEMO_FILE, 'w', encoding='utf-8'), indent=4)

    return redirect(url_for('memo.index'))


@memo_blueprint.route('/memo/list/suggest', methods=['POST'])
def suggest_memo_list():
    """
    メモリストを取得し編集するためのルート。メモリストを取得するPOSTリクエストを処理します。
    パラメーター: なし
    戻り値: メモページへのリダイレクト
    """

    key = request.form.get('key', None)
    if key is not None:
        app.config['memo_dict'].pop(key)

        json.dump(app.config['memo_dict'], open(
            MEMO_FILE, 'w', encoding='utf-8'), indent=4)

    return redirect(url_for('memo.index'))


@memo_blueprint.route('/memo/get/memo_dict', methods=['GET'])
def get_memo_dict():
    """
    メモリストを取得するためのルート。メモリストを取得するGETリクエストを処理します。
    パラメーター: なし
    戻り値: メモリストのjson文字列
    """
    json.dump(app.config['memo_dict'], open(
        MEMO_FILE, 'w', encoding='utf-8'), indent=4)
    return json.dumps(app.config['memo_dict'])


if __name__ == '__main__':
    app.run(debug=True)
