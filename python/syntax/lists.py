if __name__ == '__main__':
    N = int(input())
    resultList = []
    for x in range(N):
        command = str(input())
        if "append" in command:
            resultList.append(int(command[7:]))
        elif "print" in command:
            print(resultList)
        elif "remove" in command:
            resultList.remove(int(command[7:]))
        elif "pop" in command:
            resultList.pop()
        elif "sort" in command:
            resultList.sort()
        elif "insert" in command:
            resultList.insert(int(command[7:8]), int(command[9:]))
        else:
            resultList.reverse()
