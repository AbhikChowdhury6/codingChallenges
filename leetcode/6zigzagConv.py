from icecream import ic

def conv(s,num_rows):
    def get_forl_row(s, num_rows, start_idx):
        first_row = []
        next_idx = start_idx
        while next_idx < len(s):
            first_row.append(s[next_idx])
            next_idx += (2*num_rows) - 2 if num_rows > 1 else 1
        return "".join(first_row)
    
    def get_mid_row(s, num_rows, row_num):
        this_row = []
        next_idx = row_num
        short_jump = 2*row_num
        long_jump = (2*num_rows - 2) - short_jump
        
        while next_idx < len(s):
            this_row.append(s[next_idx])
            next_idx  += long_jump
            if next_idx >= len(s):
                break
            this_row.append(s[next_idx])
            next_idx  += short_jump
        return "".join(this_row)
        
    
    firstRow = get_forl_row(s, num_rows, 0)
    str_to_return = firstRow

    if num_rows == 1:
        return str_to_return

    for row_num in range(1, num_rows - 1):
        next_row = get_mid_row(s, num_rows, row_num)
        str_to_return += next_row

    last_row = get_forl_row(s, num_rows, num_rows-1)
    str_to_return += last_row
    return str_to_return
    


print(conv("A", 1))
print("PAHNAPLSIIGYIR")