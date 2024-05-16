# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

n = int(input())

Student = namedtuple("Student", [*input().split()])

sl = []

for _ in range(n):
    sl.append(Student(*input().split()))

print(sum(int(x.MARKS) for x in sl)/len(sl))