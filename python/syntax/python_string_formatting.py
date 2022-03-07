def print_formatted(number):
    print(*["{0:{1}} {0:{1}o} {0:{1}X} {0:{1}b}".format(n, len("{0:b}".format(number))) for n in range(1, number+1)], sep='\n')
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
