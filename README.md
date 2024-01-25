# taskApp

## 開発における注意事項
- 編集する時はbrunch分けをすること

## 主な機能
- ToDo
- リマインド機能（余裕があれば）
- メモ
- ポモドーロタイマー
- メモやToDoの内容を保持

## 操作方法・画面の説明
- 

## 役割分担
- メモ
  - (flask側)　k22084　田島夢大
flaskを使用して構築されたシンプルなメモアプリケーションの作成。
ユーザーはWebブラウザを通じてメモを作成し、表示する。
- タイマー
  - (html&js側) 担当:k22018 岩城大和 
      ポモドーロタイマーの実装とデータをflaskへ送信する機能の実装。
      作業時間25分,休憩時間5分を交互に繰り返すタイマーを作成する。
      作業を開始した時間や終えた時間(中断した場合は中断した時間)などのタイマーの作動ログを、flask側へ送信する。
- ToDo
  - (flask側)担当：k22124松浦茜　todoリスト機能の実装。項目の更新、削除などの機能を作成。

## ディレクトリ構成
```
.
├── README.md
├── instance
│   └── todo.sqlite
├── k22084 _作業報告.md
├── main.py
├── modules
│   ├── __init__.py
│   ├── __pycache__
│   │   └── memo.cpython-311.pyc
│   ├── memo.py
│   ├── pomodoro.py
│   ├── remind.py
│   └── todo.py
├── static
│   ├── data
│   ├── images
│   ├── scripts
│   │   ├── memo.js
│   │   ├── pomodoro.js
│   │   ├── remind.js
│   │   ├── script.js
│   │   └── todo.js
│   └── style.css
└── templates
    ├── index.html
    ├── memo.html
    ├── memo_create_form.html
    ├── pomodoro.html
    ├── remind.html
    └── todo.html
```