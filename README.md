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
- ToDo
 - (flask側)担当：k22124松浦茜　todoリスト機能の実装。項目の更新、削除などの機能を作成。

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
