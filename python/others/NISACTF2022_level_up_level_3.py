import requests, re
import hashlib
import urllib.parse
from urllib.request import urlopen
url = "http://localhost:1414/Level___3.php"
url2 = "localhost/md5test.php"
s = requests.Session()

# sha1file_1 = open("/Users/runfeng/Downloads/shattered-1.pdf", 'rb')
sha1file_1 = open("/Users/runfeng/Downloads/sha1_1.html", 'rb')
array1 = sha1file_1.read()
sha1file_2 = open("/Users/runfeng/Downloads/sha1_2.html", 'rb')
array2 = sha1file_2.read()
# sha1file_2 = open("/Users/runfeng/Downloads/shattered-2.pdf", 'rb')

print(hashlib.sha1(array1).digest())
print(hashlib.sha1(array2).digest())

# param={"array1":urlopen("https://github.com/bl4de/ctf/raw/master/2017/BostonKeyParty_2017/Prudentialv2/sha1_1.html"),"array2":urlopen("https://github.com/bl4de/ctf/raw/master/2017/BostonKeyParty_2017/Prudentialv2/sha1_2.html")}

param={"array1":array1,"array2":array2}
get_result=s.post(url, data=param)
print(get_result)
print(get_result.text)
