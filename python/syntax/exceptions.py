for _ in range(int(input())):
    try:
        a, b = input().split()
        print(int(int(a)/int(b)))
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")
    except ValueError:
        print("Error Code: invalid literal for int() with base 10: '{}\'".format(b if a.isdecimal() else a))
