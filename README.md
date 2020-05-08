# tips
### notebook_merge_audio_from_gcs
- GCS上にある音声ファイルをダウンロード(client library利用)
- 音声ファイルをwaveライブラリで結合

### notebook_speech_to_text_from_gcs
- GCS上にある音声ファイルをURI指定してSpeechAPIに投げて、結果を複数取得（最大30）

### notebook_firestore_read_write
- GCP firestore内にあるデータを読み込み書き込み
- firestoreのサブコレクションのデータの取得

### notebook_nuance_recognition
- Nuance VocalPasswordサーバへの声紋認証

### notebook_empath_python
- make_audio_for_empathで、音声ファイル作成
- empath_testで対象音声ファイルをempath API V2にリクエスト

### tool_python
- 各種ライブラリを使ってみる
  - contextlib (contextlib_test.py / contextlib_test2.py)
    - 特定処理の前後処理を簡単に定義できる
    - デコレータで呼ぶこともできるし、with句で呼ぶこともできる。
    
  - contextlib.ContextDecorator (contextdec_test.py)
    - クラスで前後処理 ```__enter__```、```__exit__```で定義することで、上記処理を分かりやすく書ける
    
  - contextlib.suppress (contextsup_test.py)
  - contextlib.ExitStack (contextexit_test.py)
    - callback処理で関数の最後に実行する処理を設定できる
    - 関数の最後に実行する内容が分かりやすいため大規模ＰＪ等だと使うことが多い
  - io.BytesIO / ZipFile / requests
    - 外部URLにリクエストしてzipをダウンロード。ローカルに保存せず、インメモリで解凍および、結果取得する
  - collections
    -  
