from app.config import OPENAI_API_KEY
from openai import OpenAI

# OpenAI クライアントの初期化
client = OpenAI(
    api_key=OPENAI_API_KEY
)

def transcribe_audio(file_path):
    """
    Whisper APIを使って音声を書き起こす。
    """
    with open(file_path, "rb") as audio_file:
        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )
    return transcript.text

def generate_meeting_summary(transcript, user_prompt):
    """
    OpenAI GPTを使って会議内容を要約。
    """
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "以下の会議内容を議事録形式で要約してください。"},
            {"role": "user", "content": f"{user_prompt}\n\n{transcript}"}
        ]
    )
    return response.choices[0].message.content