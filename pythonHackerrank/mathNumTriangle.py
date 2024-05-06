for i in range(1, 9): #More than 2 lines will result in 0 score. Do not leave a blank line also
    #print(10**(i-1) + 10**(i-2) + 10**(i-3) + 10**(i-4) + 10**(i-5) + 10**(i-6) + 10**(i-7) + 10**(i-8))
    print(i * int(((10**i) - 1)/9))
    #print(int(i * (10**(i-1) + 10**(i-2) + 10**(i-3) + 10**(i-4) + 10**(i-5) + 10**(i-6) + 10**(i-7) + 10**(i-8))))
    
    
    #(i * 10 ^ 0) + i                   1
    #(i * 10 ^ 1) + i                   2
    #(i * 10 ^ 2) + (i * 10 ^ 1) + i    3
        # = i * (10^2 + 10^1 + 1)       3
    #i * (10^3 + 10^2 + 10^1 + 1)       4
    #i * (10^4 + 10^3 + 10^2 + 10^1 + 10^0)
    

    #a better solution would be
    #i * (((10^i) - 1)/9)