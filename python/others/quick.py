import requests, re

url = "https://1239-49bbc869-4451-4b2b-8913-59251acce780.do-not-trust.hacking.run/"
s = requests.session()
# get the GET result
get_result= s.get(url)
# use regular expression to find out the first result which end with pattern "</p>"
result = eval((re.findall("\S*(?=</p>)", get_result.text))[0])
post_result = s.post(url, data = {"result" : result})
print(post_result.text)
