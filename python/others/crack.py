import re
import hashlib
raw = open("/usr/share/john/password.lst", "r")
hash = open("./hashed", "a")

while True:
    passwd = raw.readline()
    if len(passwd) == 0:
        break
    if re.findall("^(#!comment:/s)", passwd):
        continue
    hash.write((hashlib.md5(passwd.encode())).hexdigest() + ' ' + passwd)
raw.close()
hash.close()
