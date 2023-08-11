# benesse_hackathon
benesseハッカソンで個人開発したユーザのニーズや状況を考慮した教育コンテンツ推薦システム
## 推薦プロセス
・簡単なアンケートに答える

・全てのユーザのアンケートとの類似度を算出

・最も類似度が高いユーザの評価したコンテンツを評価が高い順に推薦
## 使用技術
Docker環境上で以下の2つに対応したコンテナを用意し、docker-composeでスタック

・バックエンド：Flask(Python)

・データベース：MySQL

## 画面
・アンケートフォーム
![スクリーンショット 2023-08-12 1 33 52](https://github.com/ssizawa/benesse_hackathon/assets/107198960/b966be3d-a099-4f61-a0a0-6057d5519fc6)

・推薦一覧
![スクリーンショット 2023-08-12 1 34 40](https://github.com/ssizawa/benesse_hackathon/assets/107198960/909fffa7-c2da-4bad-b46d-ceb34448dcb1)

## 使用方法
起動：docker-compose up -d --build

停止：docker-compose down
