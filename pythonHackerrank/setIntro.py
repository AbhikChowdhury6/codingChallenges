def average(array):
    # your code goes here
    #print(set(array))
    #print(sum(set(array)))
    val = sum(set(array))/len(set(array))
    return(float(f"{val:.3f}"))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)