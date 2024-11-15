import streamlit as st
from app.utils import transcribe_audio, generate_meeting_summary
import os

# CSS スタイリング
st.markdown("""
<style>
body {
    color: #fff;
    background-color: #111;
}
.stTextInput, .stButton, .stTextArea, .stFileUploader {
    width: 100%;
}
.stButton>button {
    color: #4CAF50;
    border: 2px solid #4CAF50;
}
</style>
""", unsafe_allow_html=True)

# タイトルと説明
st.title("Google Meet 議事録生成ツール")
st.write("MP3ファイルをアップロードして、WhisperとGPTを利用した議事録を生成します。")

# ファイルアップロードとプロンプト入力のレイアウト
col1, col2 = st.columns(2)
with col1:
    audio_file = st.file_uploader("音声ファイルをアップロード (MP3形式)", type=["mp3"])
with col2:
    user_prompt = st.text_area(
        "議事録スタイルや要約の指示を入力してください",
        "以下の会議内容を簡潔に要約してください。"
    )

# ボタンが押されたときの処理
if st.button("議事録を生成"):
    if audio_file is not None:
        # 一時保存ディレクトリを確認・作成
        temp_dir = "data/temp"
        os.makedirs(temp_dir, exist_ok=True)
        file_path = os.path.join(temp_dir, audio_file.name)

        # アップロードされたファイルを保存
        with open(file_path, "wb") as f:
            f.write(audio_file.read())

        with st.spinner('音声ファイルの書き起こし中...'):
            transcript = transcribe_audio(file_path)
        st.success('書き起こしが完了しました。')
        st.write("書き起こし結果:")
        st.text_area("書き起こし", transcript, height=200)

        with st.spinner('議事録を生成中...'):
            summary = generate_meeting_summary(transcript, user_prompt)
        st.success('議事録の生成が完了しました。')
        st.write("生成された議事録:")
        st.text_area("議事録", summary, height=300)

        # 処理結果を保存
        output_dir = "data/processed"
        os.makedirs(output_dir, exist_ok=True)
        summary_file = os.path.join(output_dir, f"{audio_file.name.split('.')[0]}_summary.txt")
        with open(summary_file, "w") as f:
            f.write(summary)

        st.success(f"議事録を保存しました: {summary_file}")
    else:
        st.error("音声ファイルをアップロードしてください！")