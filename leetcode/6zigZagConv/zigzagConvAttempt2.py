from icecream import ic

def conv(s,num_rows):    
    jump_dist = (2*num_rows) - 2 if num_rows > 1 else 1
    str_to_return = s[::jump_dist]
    if num_rows == 1:
        return str_to_return

    for row_num in range(1, num_rows - 1):
        long_jumps = s[row_num::jump_dist]
        
        first_short_idx = jump_dist - row_num
        if len(s) > first_short_idx:
            short_jumps = s[first_short_idx::jump_dist]
            next_row = "".join([x + y for x, y in zip(long_jumps, short_jumps)])
            next_row += long_jumps[-1] if len(long_jumps) > len(short_jumps) else ""
        else:
            next_row = long_jumps
        str_to_return += next_row

    str_to_return += s[num_rows-1::jump_dist]
    return str_to_return
    

#PAYPALISHIRING
print(conv("PAYPALISHIRING", 4))
print("PAHNAPLSIIGYIR")