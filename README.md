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

## 実装内容
- app -> 
