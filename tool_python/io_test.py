import io

import requests
import zipfile

# with open('./a.txt', 'w') as f:
#     f.write('test!!')

# with open('./a.txt', 'r') as f:
#     print(f.read())


# インメモリにデータを読み込んで表示
# f = io.BytesIO()
# f.write(b'test string')
# f.seek(0)
# print(f.read())


# 外部のURLからデータをダウンロードして実行
url = ('https://files.pythonhosted.org/packages/b5/96/'
        'af1686ea8c1e503f4a81223d4a3410e7587fd52df03083de24161d0df7d4/'
        'setuptools-46.1.3.zip')

f = io.BytesIO()
r = requests.get(url)
f.write(r.content)

with zipfile.ZipFile(f) as z:
    with z.open('setuptools-46.1.3/README.rst') as r:
        print(r.read().decode())
