nm, array, A, B, happiness = ([int(x) for x in input().split()], [int(x) for x in input().split()], {int(x) for x in input().split()}, {int(x) for x in input().split()}, 0)
for value in array:
    change = 1 if value in A else -1 if value in B else 0
    happiness += change
print(happiness)
