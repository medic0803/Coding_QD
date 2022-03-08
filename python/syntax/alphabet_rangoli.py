def print_rangoli(size):
    # your code goes here
    pattern = [chr(ord('a') + s) for s in range(size-1,-1,-1)]
    pattern_alignment = [('-'.join(pattern[:c+1] + (pattern[:c])[::-1])).center(4 * size - 3, '-') for c in range(size)]
    print('\n'.join(pattern_alignment + pattern_alignment[:size-1][::-1]))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
