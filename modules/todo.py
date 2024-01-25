from flask import (
    Flask,
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    jsonify,
    current_app,
)
from flask_sqlalchemy import SQLAlchemy
import os

# Flask Blueprintの作成
todo_bp = Blueprint("todo", __name__)

# SQLAlchemyの初期化
db = SQLAlchemy()


# Taskクラスの定義
class Task(db.Model):
    __tablename__ = "tasks"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.Text())
    status = db.Column(db.Integer)


# データベーステーブルを作成する関数
def create_tables():
    with current_app.app_context():
        db.create_all()


# ファイルにデータを保存する関数
def save_to_file(file_path, data):
    with open(file_path, "w") as file:
        file.write(data)


# ホームページのルート
@todo_bp.route("/")
def index():
    tasks = Task.query.all()
    return render_template("todo.html", tasks=tasks)


# 新しいタスクの追加ルート
@todo_bp.route("/new", methods=["POST"])
def new():
    task = Task()
    task.text = request.form["new_text"]
    task.status = 0
    db.session.add(task)
    db.session.commit()
    return redirect(url_for("todo.index"))


# 完了処理ルート
@todo_bp.route("/complete", methods=["POST"])
def complete():
    id = request.form["id"]
    task = Task.query.filter_by(id=id).first()
    task.status = 1
    db.session.commit()
    return redirect(url_for("todo.index"))


@todo_bp.route("/toggle_complete", methods=["POST"])
def toggle_complete():
    id = request.form["id"]
    task = Task.query.filter_by(id=id).first()
    task.status = int(request.form["checked"])
    db.session.commit()
    return redirect(url_for("todo.index"))


# 更新処理ルート
@todo_bp.route("/update", methods=["POST"])
def update():
    id = request.form["id"]
    text = request.form["text"]
    task = Task.query.filter_by(id=id).first()
    task.text = text
    db.session.commit()
    return redirect(url_for("todo.index"))


# 削除処理ルート
@todo_bp.route("/delete", methods=["POST"])
def delete():
    id = request.form["id"]
    task = Task.query.filter_by(id=id).first()
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("todo.index"))


# APIエンドポイントのルート
@todo_bp.route("/api/get_data")
def get_data():
    tasks = Task.query.all()
    task_list = [
        {"id": task.id, "text": task.text, "status": task.status} for task in tasks
    ]
    return jsonify(task_list)


@todo_bp.route("/api/sync_json")
def sync_json():
    print("get_data", flush=True)
    # データベースから全てのタスクを取得し、JSON形式でクライアントに返す
    tasks = Task.query.all()
    task_list = [
        {
            "id": task.id,
            "text": task.text,
            "status": task.status,
            # "extra": task.extra if task.extra != None else "",
        }
        for task in tasks
    ]
    # print(tasks.__dict__.values())
    # # return jsonify(tasks.__dict__)
    # return "a"
    return task_list


@todo_bp.route("/json/all")
def json_all():
    tasks = Task.query.all()
    return jsonify(
        [
            {
                "id": task.id,
                "text": task.text,
                "status": task.status,
                # "extra": task.extra if task.extra != None else "",
            }
            for task in tasks
        ]
    )


# FlaskアプリケーションをBlueprintで初期化する関数
def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "secret_key"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.sqlite"
    db.init_app(app)
    # BlueprintをFlaskアプリケーションに登録
    app.register_blueprint(todo_bp, url_prefix="/todo")
    with app.app_context():
        create_tables()
    return app


# app = Flask(__name__) の行を削除
# create_app 関数を使ってアプリケーションオブジェクトを作成
app = create_app()

# アプリケーションを実行
if __name__ == "__main__":
    app.run(debug=True, host=os.getenv("APP_ADDRESS", "localhost"), port=8001)
