# 質問類似度チェックAI

## プロジェクト概要
このプロジェクトは、質問の類似度を判定する AI アプリケーションです。  
Word2Vec を活用し、ユーザーの入力した質問が既存の質問とどの程度類似しているかを判定します。  
閾値を超える場合、既存の質問を使用するように提案します。

## 主な機能
- 質問のベクトル化（Word2Vec を使用）
- コサイン類似度の計算（scikit-learn を使用）
- しきい値を超えた場合、類似した質問を提案

## 使用技術
- **プログラミング言語**: Python
- **ライブラリ**:
  - `gensim`（Word2Vec モデルの学習）
  - `scikit-learn`（類似度計算）
  - `numpy`（数値計算）
  - `janome.tokenizer`（日本語分かち書き）

## インストール方法
### 環境の準備
以下のコマンドを実行し、必要なパッケージをインストールしてください。
```bash
pip install gensim scikit-learn numpy jieba
```

## 実行方法
```bash
python textSimilarityJpn.py
```

## コードの使い方
```
# ユーザーの質問を入力
new_question = input("あなたの質問を入力してください：")

# 既存の質問と比較
similar_question = check_similarity(new_question, question_bank, model)

# 類似度が高い質問があれば提案
if similar_question:
    print(f"既存の質問を使用することをお勧めします：{similar_question}")
else:
    print("あなたの質問は新しいものです。データベースに追加できます。")
```

## 貢献
このプロジェクトへの貢献は歓迎します。バグ報告、改善提案などがあれば、Issue を作成してください。

## デモ
<img width="424" alt="image" src="https://github.com/user-attachments/assets/a4eb4207-5a4f-4ddc-b0ca-900a9927e425" />
<img width="424" alt="image" src="https://github.com/user-attachments/assets/03338b78-059b-40d5-987e-e0527f037ac9" />



連絡先  
開発者: リ  
E-mail: liyinan.jl@gmail.com  
GitHub: https://github.com/Li244228  

