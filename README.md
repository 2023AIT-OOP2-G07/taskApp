# taskApp

## 主な機能
- ToDo
- リマインド機能
- メモ
- ポモドーロタイマー
- メモやToDoの内容を保持

## 役割分担
- UI（画面デザイン・レイアウト）
- タイマー
- メモ（テキストボックス）
- ToDo
  - リマインド
  - カレンダー
- 保存

## ディレクトリ構成
```
.
├── README.md
├── app
│   ├── __init__.py
│   ├── scripts
│   │   ├── memo.js
│   │   ├── pomodoro.js
│   │   ├── remind.js
│   │   ├── script.js
│   │   └── todo.js
│   ├── static
│   │   ├── images
│   │   └── style.css
│   └── templates
│       ├── index.html
│       ├── memo.html
│       ├── pomodoro.html
│       ├── remind.html
│       └── todo.html
├── config.py
├── requirements.txt
├── run.py
└── venv
```

## 実装内容
- app -> 