import numpy
N, M, P = map(int, input().split())
print(numpy.concatenate((numpy.array([list(map(int, input().split())) for _ in range(N)]), numpy.array([list(map(int, input().split())) for _ in range(M)]))))

