wordlist = open("./hashed", "r")

hashed = input()

while True:
    entry = wordlist.readline()
    if len(entry) == 0:
        break
    if hashed == entry.split()[0]:
        print("Plaintext is :" + entry.split()[1])
        break
wordlist.close()
