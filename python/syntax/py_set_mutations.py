a, A, N = [int(input()), set(map(int, input().split())), int(input())]
for x in range(N):
    command = (input().split())[0]
    getattr(A, command)(set(map(int, input().split())))
print(sum(A)) 
