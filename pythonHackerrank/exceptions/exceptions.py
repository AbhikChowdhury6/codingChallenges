# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

for _ in range(n):
    try:
        a,b = map(int, input().split())
        c = a//b
        print(c)
    except ZeroDivisionError as e:
        print("Error Code: " + str(e))
    except ValueError as e:
        print("Error Code: " + str(e))