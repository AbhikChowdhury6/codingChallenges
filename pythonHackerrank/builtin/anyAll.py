# Enter your code here. Read input from STDIN. Print output to STDOUT
_ = input()

inNums = list(map(int, input().split()))

isPal = lambda x: [*str(x)] == list(reversed([*str(x)]))

#print(list(map(isPal, inNums)))
#print(any(map(isPal, inNums)))
#print(inNums)
#print(list(map(lambda x: x>=0, inNums)))
#print(all(map(lambda x: x>=0, inNums)))

print(all(map(lambda x: x>=0, inNums)) and any(map(isPal, inNums)))