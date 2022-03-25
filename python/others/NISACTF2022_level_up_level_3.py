import requests, re
import hashlib
import urllib.parse
from urllib.request import urlopen
url = "http://120.27.195.236:28991/Level___3.php"
url2 = "localhost/md5test.php"
s = requests.Session()

# sha1file_1 = open("/Users/runfeng/Downloads/shattered-1.pdf", 'rb')
sha1file_1 = open("/Users/runfeng/Downloads/sha1_1.html", 'rb')
array1 = sha1file_1.read()
sha1file_2 = open("/Users/runfeng/Downloads/sha1_2.html", 'rb')
array2 = sha1file_1.read()
# sha1file_2 = open("/Users/runfeng/Downloads/shattered-2.pdf", 'rb')

print(hashlib.sha1(array1).digest())
print(hashlib.sha1(array2).digest())

# param={"array1":urlopen("http://shattered.io/static/shattered-1.pdf"),"array2":urlopen("http://shattered.io/static/shattered-2.pdf")}

param={"array1":array1,"array2":array2}
get_result=s.post(url, data=param)
print(get_result)
print(get_result.text)
