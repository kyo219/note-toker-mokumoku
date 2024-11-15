# note-toker-mokumoku

このプロジェクトは、音声ファイルから議事録を自動生成するツールです。Whisper APIを使用して音声をテキストに変換し、その後OpenAIのGPTを用いて要約を行います。


## HOW TO USE

1. google chrome の拡張機能で会議を保存する
https://chromewebstore.google.com/detail/kfokdmfpdnokpmpbjhjbcabgligoelgp

<img width="1420" alt="スクリーンショット 2024-11-15 18 48 01" src="https://github.com/user-attachments/assets/7ba262be-8e9f-4034-a3a4-99201d14c24a">

<img width="721" alt="スクリーンショット 2024-11-15 18 49 01" src="https://github.com/user-attachments/assets/9c11c321-6899-402e-9f14-f50383fa1394">

2. 書き起こし, 要約
1. がローカルにダウンロードできるので, このページにupload
https://github.com/user-attachments/assets/41659505-f5f3-4255-8824-77e9b0319ac6

3. api連携で, txtを飛ばす
これから実装予定

4. デプロイ
まだ

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
