"""
REST

HTTPメソッド　クライアントが行いたい処理をサーバに伝える

GET データの参照
POST データの新規登録
PUT データの更新
DELETE データの削除
"""

import urllib.request
import json

payload = {'key1': 'value1', 'key2': 'value2'}

url = 'http://httpbin.org/get' + '?' + urllib.parse.urlencode(payload)
with urllib.request.urlopen(url) as f:
    r = json.loads(f.read().decode('utf-8'))

print(r)