# what do we need to do

# make a function with the one parameter
    # calls a function that carries the parameter of interest and the recursive function
    # define the recursive function when calling the parameter


#what we actually need to do
#make a lambda that takes in function that calls itself and pass in the recursive function wrap all that and give it the parameter

l = [1, 2, 3]
l2 = [l, l, l]
l3 = [l2, l2, l2]


print(l3)


part1 = (lambda recurFunc : lambda recurVals : recurFunc(recurFunc, recurVals))

part2 = part1((lambda fl, y: [x for b in y for x in fl(fl,b)] if type(y) is list else [y]))

def part2func (fl, y):
    if type(y) is not list:
        return [y]
    o = []
    for b in y:
        for x in part2func(fl,b):
            o.append(x)
    return o

part2def = part1(part2func)


print(part2(l3))

print(part2def(l3))

print(sum(l3, []))

part2fib = part1((lambda s,x:1 if x==0 else x*s(s,x-1)))

print(part2fib(10))

#a = (lambda g: (lambda f, *a: f(f, *a))(lambda fl, y: [x for b in y for x in fl(fl,b)] if type(y) is list else [y]))(l2)

#print(a)

#(lambda n: (lambda f, *a: f(f, *a))(lambda rec, n: 1 if n == 0 else n*rec(rec, n-1), n))
