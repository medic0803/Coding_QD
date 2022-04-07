def minion_game(string):
    vowels = 'AEIOU'
    Stuart = 0
    Kevin = 0
    length = len(string)
    for n in range(length):
        if string[n] in vowels:
            Kevin += length - n
        else:
            Stuart += length - n
    print("Stuart " + str(Stuart)) if Stuart > Kevin else print("Draw") if Stuart == Kevin else print("Kevin " + str(Kevin))
if __name__ == '__main__':
    s = input()
    minion_game(s)
