# おたすけタスク

## コンセプト
### シンプルで汎用性のある3in1思考整理アプリケーション
- 複数のアプリを開かなくていい
- 複雑な機能はなく、わかりやすい

## 主な機能
- ToDoリスト
- ~~リマインド機能（余裕があれば）~~
- メモ
- ポモドーロタイマー
- メモやToDoの内容を保持
- ポモドーロタイマーのログを保持

## 操作方法・画面の説明
- メモ
  - aa

- ポモドーロタイマー
  - aa

- ToDoリスト
  - aa

<br>
<br>
<br>

### 以下開発関連↓↓

## 開発における注意事項
- 編集する時はbrunch分けをすること

## 役割分担
- メモ
  - (flask側)　k22084　田島夢大
    - flaskを使用して構築されたシンプルなメモアプリケーションの作成。
    - ユーザーはWebブラウザを通じてメモを作成し、表示する。
  - (html&js側) k22113 藤田力弥
    - サイトのWebブラウザ部分を作成
    - 新規メモのタイトル・本文を受け取り、サーバーへ送信する機能の実装
    - メモのリストから任意のメモを再編集できる機能を実装
    - メモのリストから任意のメモを削除するようにサーバーへ送信する機能の実装
- タイマー
  - (html&js側) 担当:k22018 岩城大和 
      - ポモドーロタイマーの実装とデータをflaskへ送信する機能の実装。
      - 作業時間25分,休憩時間5分を交互に繰り返すタイマーを作成する。
      - 作業を開始した時間や終えた時間(中断した場合は中断した時間)などのタイマーの作動ログを、flask側へ送信する。
- ToDo
  - (flask側)担当：k22124松浦茜　
    - todoリスト機能の実装。項目の更新、削除などの機能を作成。

- 全体統括(K22050 小西秀斗)
  - リポジトリ、READMEの管理
  - コンセプト等、方向性の決定
  - base.htmlの作成
  - 発表資料の作成
  - 発表

## ディレクトリ構成
```
.
├── README.md
├── instance
│   └── todo.sqlite
├── main.py
├── modules
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-311.pyc
│   │   ├── memo.cpython-311.pyc
│   │   ├── pomodoro.cpython-311.pyc
│   │   └── todo.cpython-311.pyc
│   ├── memo.py
│   ├── pomodoro.py
│   └── todo.py
├── pyproject.toml
├── static
│   ├── data
│   │   ├── memo_data.json
│   │   ├── pomodoro.json
│   │   └── todo_data.json
│   ├── scripts
│   │   ├── memo.js
│   │   ├── pomodoro.js
│   │   └── todo.js
│   └── style.css
└── templates
    ├── index.html
    ├── memo.html
    ├── memo_create_form.html
    ├── pomodoro.html
    └── todo.html
```