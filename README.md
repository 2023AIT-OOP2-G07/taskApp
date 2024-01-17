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

## 作業内容

- グループで作りたいアプリを決めた
- ファイルの構成を小西秀斗さんと話し合って決めた

## グループ内でお世話になった人2~3名を理由とともに理由とともに挙げる

- リーダーの欠席で進行役としてとしてグループの話し合いを進めてくれた(K21233 鳥海匠見)
- グループで分担して開発する時に使えるflaskの機能について教えてくれた(K22097 仁木正人)

## 振り返り（感想含む）と次回までの作業予定

- 役割分担やファイル構成を先に決めることができてよかった
- 来週から分担作業を進めることができる
- 次回からはメモアプリの実装を田島さんと一緒に開発をする予定