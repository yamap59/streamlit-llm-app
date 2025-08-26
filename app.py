from dotenv import load_dotenv
from openai import OpenAI
import streamlit as st
import os

# .envファイルの内容を環境変数として読み込む
load_dotenv()
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

def call_chat_completion_api(system_message, user_message):
    client = OpenAI(api_key=OPENAI_API_KEY)
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_message}
        ],
        temperature=0.5
    )

    return completion.choices[0].message.content

def main():
    st.title("プログラミングコースAIチャットボット")

    st.write("##### 動作モード1: p5.jsの専門家")
    st.write("入力フォームにp5.jsに関する質問を入力して送信することで回答を得られます。")
    st.write("##### 動作モード2: 勉強法の専門家")
    st.write("入力フォームに勉強に関する質問や悩みを入力して送信することで回答を得られます。")

    selected_item = st.radio(
        "動作モードを選択してください。",
        ["p5.jsの専門家", "勉強法の専門家"]
    )

    st.divider()

    if user_message := st.chat_input("質問してみましょう"):
        if selected_item == "p5.jsの専門家":
            st.chat_message("user").markdown(user_message)
            ai_message = call_chat_completion_api(
                system_message="あなたはp5.jsの専門家です。初心者にもわかりやすく、具体的に、丁寧に説明してください。",
                user_message=user_message
            )
            st.chat_message("assistant").markdown(ai_message)
        else:
            st.chat_message("user").markdown(user_message)
            ai_message = call_chat_completion_api(
                system_message="あなたは勉強法の専門家です。初心者にもわかりやすく、具体的に、丁寧に説明してください。",
                user_message=user_message
            )
            st.chat_message("assistant").markdown(ai_message)

main()