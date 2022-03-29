number = int(input())
roomList = input().split()
seen = set()
dupli = set()
for roomNum in roomList:
    if roomNum not in seen:
        seen.add(roomNum)
    else:
        dupli.add(roomNum)        
print((seen.difference(dupli)).pop())
