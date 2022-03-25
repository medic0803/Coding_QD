import requests, re
import hashlib
url = "http://120.27.195.236:28991/level_2_1s_h3re.php"
url2 = "localhost/md5test.php"
s = requests.Session()

array1 = "d131dd02c5e6eec4693d9a0698aff95c2fcab58712467eab4004583eb8fb7f8955ad340609f4b30283e488832571415a085125e8f7cdc99fd91dbdf280373c5bd8823e3156348f5bae6dacd436c919c6dd53e2b487da03fd02396306d248cda0e99f33420f577ee8ce54b67080a80d1ec69821bcb6a8839396f9652b6ff72a70"
array2 = "d131dd02c5e6eec4693d9a0698aff95c2fcab50712467eab4004583eb8fb7f8955ad340609f4b30283e4888325f1415a085125e8f7cdc99fd91dbd7280373c5bd8823e3156348f5bae6dacd436c919c6dd53e23487da03fd02396306d248cda0e99f33420f577ee8ce54b67080280d1ec69821bcb6a8839396f965ab6ff72a70"
result1 = bytes.fromhex(array1)
result2 = bytes.fromhex(array2)
print(hashlib.md5(result1).digest())
print(hashlib.md5(result2).digest())
param={"array1":result1,"array2":result2}
get_result=s.post(url, data=param)
print(get_result)
print(get_result.text)
