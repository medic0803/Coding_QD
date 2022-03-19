import requests, re

url = "https://1239-e39bb701-ed06-4211-90bc-cabd6f666121.do-not-trust.hacking.run"
s = requests.Session()

def getURL(url):
    con = s.get(url)
    res = con.text
    return res

def Calculation(text):
    result = eval(((re.findall(".*</p>", text))[0])[0:-4])
    return result

def postRES():
    result = Calculation(getURL(url))
    payload = {"result":result}
    r = s.post(url, data=payload)
    print(type(r))
    print(r)
    return r

print(postRES().text)
