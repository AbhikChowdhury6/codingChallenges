cube = lambda x: x**3  # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    if n == 0: return []
    if n == 1: return [0]
    out = [0,1]
    for i in range(2, n):
        out.append(out[i-1] + out[i-2])
    return out

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))