from flask import Flask, render_template, request, redirect, url_for, Blueprint, jsonify
from datetime import datetime
import json

pomodoro_blueprint = Blueprint("pomodoro", __name__)




from flask import Blueprint, render_template

pomodoro_bp = Blueprint('pomodoro', __name__)

@pomodoro_bp.route('pomodoro/get', methods=['GET'])
def get():  # 関数名は重複していなければなんでもよい
    result = ""
    # ローカルのファイルを全部読み込んで返すだけ
    with open("./static/data/pomodoro.json", mode='r') as f:
        json_load = json.load(f)
        log = josn_load["log"]
    return jsonify({"log" : log })

@pomodoro_bp.route('pomodoro/post', methods=['GET'])
def post():
    result = request.json()
    # パラメータをローカルのファイルに書き込むだけ
    with open("./static/data/pomodoro.json", mode='a') as f:
        json.dump(result, f, indent = 2)
    return 200
    
