row, column = map(int, input().split())
pattern = [('.|.' * n).center(column, '-') for n in range(1, row - 1, 2)]    
print('\n'.join(pattern + ["WELCOME".center(column, '-')] + pattern[::-1]))

