from icecream import ic

def conv(s,num_rows):
    def get_forl_row(s, num_rows, start_idx):
        first_row = []
        next_idx = start_idx
        while next_idx < len(s):
            first_row.append(s[next_idx])
            next_idx += (2*num_rows) - 2
        return "".join(first_row)
    
    
    
    firstRow = get_forl_row(s, num_rows, num_rows-1)
    str_to_return = firstRow
    
    
    
    lastRow = get_forl_row(s, num_rows, num_rows-1)
    return get_forl_row(s, num_rows, num_rows-1)
    


print(conv("PAYPALISHIRING", 3))