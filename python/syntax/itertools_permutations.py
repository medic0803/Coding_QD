from itertools import permutations
S, K = input().split()
print('\n'.join([''.join(l) for l in permutations(sorted(S), int(K))]))
