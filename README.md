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
各種ライブラリを使ってみる
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
- collections.ChainMap
  - 複雑なdict処理を行う際は使われる
- collections.defaultdict
  - カウンターとしても使えるし、集合としても使うことができる
- collections.Counter
  - カウンターとしての利用に特化。簡単にカウンター利用できる。
  - カウントの最大のものや、トップ〇番とかを簡単に抽出できる
- queue.Queue,LifoQueue / collections.deque
  - queue.Queue [1,2,3]と入れたら、1から取得
  - queue.LifoQueue [1,2,3]と入れたら、3から取得
    - Queue/LifoQueueはマルチスレッド環境のメソッドがあるので、そういうときに使う
  - collections.deque は、Listのappendなどに比べてメモリ効率が良く、高速に処理されると言われている
```
for _ in range(3):
    ## FIFO
    print(f'FIFO queue = {q.get()}')
    ## LIFO
    print(f'FIFO queue = {lq.get()}')
    ## LIFO
    print(f'FIFO queue = {l.pop()}')
    ## FIFO
    # print(f'FIFO queue = {l.pop(0)}')
    ## LIFO
    print(f'FIFO queue = {d.pop()}')
    ## FIFO
    # print(f'FIFO queue = {d.popleft()}')
    print('')
```

```
.\tool_python\collections_deque_test.py
FIFO queue = 0
FIFO queue = 2
FIFO queue = 2
FIFO queue = 2

FIFO queue = 1
FIFO queue = 1
FIFO queue = 1
FIFO queue = 1

FIFO queue = 2
FIFO queue = 0
FIFO queue = 0
FIFO queue = 0
```

- collections.namedtuple
  - csvデータとかを入力したときに値を取り出しやすくなる
- collections.OrderedDict
  - 順番を守られた形で辞書を使いたいのであれば、これを使う。
  - データを追加すると必ず最後に入る
    - ソートをしたいなら、データをつかした後にソートを再度実行
- re (re_test.py / re_test2.py / re_test3.py)
  - match() 
    - 字列の先頭で正規表現とマッチするか判定
  - search()
    - 文字列を操作して、正規表現がどこにマッチするか調べる
  - findall()
    - 正規表現にマッチする部分文字列をすべて洗い出しリストとして返す
  - finditer()
    - 重複しないマッチオブジェクトのイテレータを返す
  - compile()
    - 正規表現ルールをコンパイルして高速処理。一度でなく複数回同じルールを処理するなら活用すべき。
  - 正規表現内でのグループ名の付け方、これをつけておくと、後で使うときに分かりやすい
    - ```(?<group名>)```　group名をregionとするなら以下のような形で取得できる
    - ```print(m.group('region'))``` 等、
    
```
s = ('arn:aws:cloudformation:us-east-2:123456789012:stack/'
    'lambda-error-processor/1134083a-2608-1e91-9897-022501a2c456')

RE_STACK_ID = re.compile(r"""
    arn:aws:cloudformation:
    (?P<region>[\w-]+):
    (?P<account>[\d]+)
    :stack/
    (?P<stackname>[\w-]+)/
    [\w-]+""", re.VERBOSE)
```

  - re.subを使って、関数と組み合わせることもできる
```
def hexrpl(match):
    value = int(match.group())
    return hex(value)

p = re.compile(r'\d')
print(p.sub(hexrpl, '12345 55 11 test test2'))
# print(re.sub(p, hexrpl, '12345 55 11 test test2'))
```
  - 正規表現でのgreedy
    - ?を使って、Greedyなmatchを防ぐこともtips
```
s = '<html><head><title>Title</title></head></html>'

print(re.match('<.*>', s))
print(re.match('<.*?>', s))
```

  - format
    - tuple、辞書のキーワード渡し、コメント入れる際とか、重宝
    - 10,16進数,8進数,2進数など、簡単に表示できる
```
# タプル
t = (1, 2, 3)
print('{t[0]} {t[2]}'.format(t=t))
print('{0} {2}'.format(*t))
```

```
# 辞書
d = {'name' : 'shinya', 'family': 'koizumi'}
print('{name} {family}'.format(**d))
```

```
# コメント入れる
print('{name:{fill}{align}{width}}'.format(name = 'test', fill = '*', align = '^', width = 30))
# 出力
# *************test*************
```

```
# 10,16進数,8進数,2進数など、簡単に表示できる
print('{0:d} {1:d} {2:d}'.format(100,200,300))
# result is 100 200 300
print('{:d} {:d} {:d}'.format(100,200,300))
# result is 100 200 300
print(int(100), hex(100), oct(100), bin(100))
# result is 100 0x64 0o144 0b1100100
print('{0:d} {0:#x} {0:#o} {0:#b}'.format(100))
# result is 100 0x64 0o144 0b1100100
print('{0:d} {0:x} {0:o} {0:b}'.format(100))
# result is 100 64 144 1100100
```

- repr関数とstr関数

```
# classの__str__関数をオーバーライドして、管理情報を表示させたり
# するのはよくやるアプリケーション開発の手法
class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return 'Point<object>'

    def __str__(self):
        return 'Point ({}, {})'.format(self.x, self.y)
    
p = Point(10,100)
print('{0!r}'.format(p))
print('{0}'.format(p))
print('{0!s}'.format(p))
```


