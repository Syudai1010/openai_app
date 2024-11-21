import os
from dotenv import load_dotenv
import openai
import streamlit as st
import tiktoken

# .envファイルから環境変数を読み込む
load_dotenv()

# OpenAI APIキーを設定
openai.api_key = os.getenv("OPENAI_API_KEY")

# Streamlitアプリのタイトル
st.title("シンプルなチャットアプリ")

# ユーザーの入力を取得
user_input = st.text_input("あなたの質問を入力してください:")

if st.button("送信"):
    if user_input:
        with st.spinner('回答を生成中...'):
            try:
                # メッセージの準備
                messages = [
                    {"role": "user", "content": user_input}
                ]

                # OpenAI APIへのリクエスト（新しいインターフェースを使用）
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=messages
                )

                # 回答の取得（新しいレスポンス構造に対応）
                answer = response['choices'][0]['message']['content'].strip()
                st.success("回答:")
                st.write(answer)

                # トークン使用量の取得（新しいレスポンス構造に対応）
                prompt_tokens = response['usage']['prompt_tokens']
                completion_tokens = response['usage']['completion_tokens']
                total_tokens = response['usage']['total_tokens']

                # 料金の計算（gpt-3.5-turboの場合）
                # 1,000トークンあたり$0.002
                cost = total_tokens / 1000 * 0.002

                # 使用トークン数と推定料金の表示
                st.write(f"**使用したトークン数:** {total_tokens} トークン (プロンプト: {prompt_tokens}, 応答: {completion_tokens})")
                st.write(f"**推定料金:** ${cost:.6f}")

            except Exception as e:
                st.error(f"エラーが発生しました: {e}")
    else:
        st.warning("質問を入力してください。")







