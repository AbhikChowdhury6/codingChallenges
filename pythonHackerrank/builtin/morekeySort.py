# Enter your code here. Read input from STDIN. Print output to STDOUT

isOdd = lambda x: x.isdigit() and int(x)% 2 == 1

inL = [*input()]

# print(inL)

SortedList = sorted(inL, reverse=True, key=lambda x: (x.islower(), x.isupper(), isOdd(x), -ord(x)))

print("".join(SortedList))