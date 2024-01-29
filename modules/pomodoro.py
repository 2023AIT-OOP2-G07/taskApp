from flask import Blueprint, render_template
from flask import request, redirect, url_for, jsonify
from datetime import datetime
import json

pomodoro_bp = Blueprint('pomodoro', __name__)

@pomodoro_bp.route('/pomodoro')
def pomodoro():
    return render_template('pomodoro.html')


@pomodoro_bp.route('/pomodoro/get', methods=['GET'])
def get():  # 関数名は重複していなければなんでもよい
    result = ""
    # ローカルのファイルを全部読み込んで返すだけ
    with open("./static/data/pomodoro.json", mode='r') as f:
        #print("test1")
        json_load = json.load(f)
        #print("test2")
        print(json_load)
        log = json_load["log"]
    return jsonify({"log" : log })

@pomodoro_bp.route('/pomodoro/post', methods=['POST'])
def post():
    result = request.json
    # パラメータをローカルのファイルに書き込むだけ
    with open("./static/data/pomodoro.json", mode='w', encoding = 'utf-8') as f:
        json.dump(result, f, indent = 2)
    return "200"
    

