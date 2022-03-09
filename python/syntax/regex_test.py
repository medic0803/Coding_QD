import re
input = "num = [2,7,11,1], target = 1239"
x = re.findall(r"(?<=\[).*(?=\])",input)
y = re.findall(r"(?<=\=\s)\d+", input)
print(x)
print(y)
