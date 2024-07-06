import qrcode

from qrcode import pyqrcode

s="https://www.youtube.com/watch?v=X27QMxozv6o"

url=pyqrcode.create(s)
url.svg=("qrcode.svg")