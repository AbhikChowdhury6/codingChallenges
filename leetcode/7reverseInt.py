import math
def reverse (x):
    isNeg = x < 0
    if isNeg: x *= -1
    less_than_nums = [2,1,4,7,4,8,3,6,4,7]
    num_didgits = math.floor(math.log(x,10)) + 1
    if num_didgits > 10: return 0

    could_be_over = True
    if num_didgits < 10: could_be_over = False

    new_num = 0
    for i in range(num_didgits):
        this_num = ((x % 10**(i+1)) // 10**i)
        
        if could_be_over and this_num > less_than_nums[i]:
            return 0
        elif could_be_over and this_num < less_than_nums[i]:
            could_be_over = False
        
        new_num += 10**(num_didgits-(i+1)) * this_num
        
    new_num *= -1 if isNeg else 1
    return new_num

print(reverse(1234567))