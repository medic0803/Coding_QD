a, b, c, d = (input(), set(input().split()), input(), set(input().split()))
print('\n'.join(sorted(b.symmetric_difference(d), key=int)))
