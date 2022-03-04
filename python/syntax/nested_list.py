if __name__ == '__main__':
    dic_sheet = dict()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        dic_sheet[name] = score
    
    lowest_2nd = sorted(list(set((dic_sheet.values()))))[1]
    student = []
    for s in dic_sheet:
        if dic_sheet[s] == lowest_2nd:
            student.append(s)
    print(*sorted(student), sep='\n')
