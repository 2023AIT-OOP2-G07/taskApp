# taskApp

## 開発における注意事項
- 編集する時はbrunch分けをすること

## 主な機能
- ToDo
- リマインド機能
- メモ
- ポモドーロタイマー
- メモやToDoの内容を保持

## 役割分担
- メモ
- タイマー
    - (html&js側) 担当:k22018 岩城大和 
      ポモドーロタイマーの実装とデータをflaskへ送信する機能の実装。
      作業時間25分,休憩時間5分を交互に繰り返すタイマーを作成する。
      作業を開始した時間や終えた時間(中断した場合は中断した時間)などのタイマーの作動ログを、flask側へ送信する。
- ToDo

## ディレクトリ構成
```
.
├── README.md
├── main.py
├── modules
│   ├── memo.py
│   ├── pomodoro.py
│   ├── remind.py
│   └── todo.py
├── static
│   ├── data
│   ├── images
│   ├── scripts
│   │   ├── memo.js
│   │   ├── pomodoro.js
│   │   ├── remind.js
│   │   ├── script.js
│   │   └── todo.js
│   └── style.css
└── templates
    ├── index.html
    ├── memo.html
    ├── pomodoro.html
    ├── remind.html
    └── todo.html
```
