import gensim
from gensim.models import Word2Vec
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from janome.tokenizer import Tokenizer  # Janomeライブラリを使う

# 1. 質問データベース（自分で拡張できます）
question_bank = [
    "あなたの好きな色は何ですか？",
    "あなたの性別は何ですか？",
    "今年はいくつですか？",
    "どんな音楽が好きですか？"
]

# 2. Janomeを使って分かち書き
tokenizer = Tokenizer()

def tokenize_japanese(text):
    # 分かち書きのために名詞を抽出
    return [token.base_form for token in tokenizer.tokenize(text) if token.part_of_speech.startswith('名詞')]

# 3. Word2Vecの学習（既存のデータを使用、実際のアプリケーションでは大量のデータで学習をお勧めします）
tokenized_questions = [tokenize_japanese(q) for q in question_bank]
model = Word2Vec(sentences=tokenized_questions, vector_size=100, window=5, min_count=1, workers=4)

# 4. 文のベクトルを取得（単語ベクトルの平均）
def get_sentence_vector(sentence, model):
    words = tokenize_japanese(sentence)
    word_vectors = [model.wv[word] for word in words if word in model.wv]
    if len(word_vectors) == 0:
        return np.zeros(model.vector_size)
    return np.mean(word_vectors, axis=0)

# 5. 新しい質問と既存の質問の類似度を計算
def check_similarity(user_input, question_bank, model, threshold=0.8):
    user_vector = get_sentence_vector(user_input, model)
    for question in question_bank:
        question_vector = get_sentence_vector(question, model)
        similarity = cosine_similarity([user_vector], [question_vector])[0][0]
        if similarity > threshold:
            print(f"⚠️ あなたの質問「{user_input}」は既存の質問「{question}」と類似しています。類似度は {similarity:.2f} です。既存の質問を使うことをお勧めします！")
            return question  # 最も類似した質問を返す
    return None  # 類似度が高い質問が見つからない場合

# 6. ユーザーの入力（iOSアプリのユーザー入力に置き換え可能）
new_question = input("あなたの質問を入力してください：")
similar_question = check_similarity(new_question, question_bank, model)
if similar_question:
    print(f"既存の質問を使用することをお勧めします：{similar_question}")
else:
    print("✅ あなたの質問は新しいものです。データベースに追加できます。")
