from flask import Flask, Blueprint, render_template, request, redirect, url_for, jsonify, current_app
import os
import json

# Flask Blueprintの作成
todo_bp = Blueprint('todo', __name__)

# データファイルのパス
data_file_path = 'todo_data.json'

# データを読み込む関数
def load_data():
    if os.path.exists(data_file_path):
        with open(data_file_path, 'r') as file:
            data = json.load(file)
        return data
    else:
        return []

# データを保存する関数
def save_data(data):
    with open(data_file_path, 'w') as file:
        json.dump(data, file)

# ホームページのルート
@todo_bp.route('/todo')
def todo():
    tasks = load_data()
    return render_template('todo.html', tasks=tasks)

# 新しいタスクの追加ルート
@todo_bp.route('/new', methods=["POST"])
def new():
    data = load_data()
    new_task = {
        'id': len(data) + 1,
        'text': request.form["new_text"],
        'status': 0
    }
    data.append(new_task)
    save_data(data)
    return redirect(url_for('todo.todo'))

# 完了処理ルート
@todo_bp.route('/complete', methods=["POST"])
def complete():
    data = load_data()
    id = int(request.form["id"])
    for task in data:
        if task['id'] == id:
            task['status'] = 1
            break
    save_data(data)
    return redirect(url_for('todo.todo'))

# 更新処理ルート
@todo_bp.route('/update', methods=["POST"])
def update():
    data = load_data()
    id = int(request.form["id"])
    text = request.form["text"]
    for task in data:
        if task['id'] == id:
            task['text'] = text
            break
    save_data(data)
    return redirect(url_for('todo.todo'))

# 削除処理ルート
@todo_bp.route('/delete', methods=["POST"])
def delete():
    data = load_data()
    id = int(request.form["id"])
    data = [task for task in data if task['id'] != id]
    save_data(data)
    return redirect(url_for('todo.todo'))

# APIエンドポイントのルート
@todo_bp.route('/api/get_data', methods=["POST"])
def get_data():
    tasks = load_data()
    return jsonify(tasks)

# FlaskアプリケーションをBlueprintで初期化する関数
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret_key'

    # BlueprintをFlaskアプリケーションに登録
    app.register_blueprint(todo_bp, url_prefix='/todo')

    return app

# create_app 関数を使ってアプリケーションオブジェクトを作成
app = create_app()

# アプリケーションを実行
if __name__ == '__main__':
    app.run(debug=True, host=os.getenv('APP_ADDRESS', 'localhost'), port=8001)
