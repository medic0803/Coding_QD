from collections import Counter
X, goods, earning = input(), dict(Counter(list(map(str, input().split())))), 0
for _ in range(int(input())):
    size, price = list(map(str, input().split()))
    if size in goods.keys() and goods[size] > 0:
        goods[size] -= 1
        earning += int(price)
print(earning)
