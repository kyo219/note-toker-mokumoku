# note-toker-mokumoku

このプロジェクトは、音声ファイルから議事録を自動生成するツールです。Whisper APIを使用して音声をテキストに変換し、その後OpenAIのGPTを用いて要約を行います。

## プロジェクト構造

```
project/
│
├── app/
│ ├── init.py # 空でOK
│ ├── app.py # Streamlitのフロントエンド部分
│ ├── utils.py # WhisperとOpenAI APIの処理を記述
│
└── data/
│ ├── temp/ # アップロードされた一時ファイルを保存
│ ├── processed/ # 処理後の議事録や書き起こしを保存
│
└── main.py # Streamlitのフロントエンド部分
└── poetry.lock
└── pyproject.toml

```


## 主な機能

- **音声アップロード**: MP3形式の音声ファイルをアップロードできます。
- **音声書き起こし**: Whisper APIを使用して音声をテキストに変換します。
- **議事録生成**: ユーザーの指示に基づいて、OpenAIのGPTを使用して議事録を生成します。

## 立ち上げ方法

1. 必要なライブラリをインストールします:
   ```bash
   poetry install
   ```
2. Streamlitアプリケーションを起動します:
   ```bash
   streamlit run main.py
   ```

アプリケーションはデフォルトで http://localhost:8501 でアクセス可能です。