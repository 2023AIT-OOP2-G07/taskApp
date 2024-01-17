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
  - 藤田力弥
    - javascript
      - 保存しているメモをPOSTで取得・表示
      - 保存ボタンを実装
    - html
      - メモアプリの構成
      - 画面の装飾
      - ほか
        
      
     
- タイマー
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
