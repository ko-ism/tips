import contextlib
import os

try:
    os.remove('somefile.tmp')
except FileNotFountError:
    pass

with contextlib.suppress(FileNotFountError):
    os.remove('somefile.tmp')