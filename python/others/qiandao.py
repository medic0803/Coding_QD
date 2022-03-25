import requests, re

url = "http://120.27.195.236:28990"
url2 = "localhost/qiandao.php"
s = requests.Session()
param2={"ahahahaha":"jitanglailo","\u202e\u2066Ugeiwo\u202e\u2066cuishiyuan":"\u202e\u2066 Flag!\u202e\u2066N1SACTF"}
get_result=s.get(url, params=param2)
# get_result=s.get(url2, params=param2)
# &+!!&
print(get_result)
print(get_result.text)
