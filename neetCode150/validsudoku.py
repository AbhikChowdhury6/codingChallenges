from icecream import ic
board = \
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]


def isValidSudoku(board) -> bool:
    valid_didgits = set([".","1","2","3","4","5","6","7","8","9"])
    
    def check_element_range(rc_pairs):
        element_counts = {}
        for r,c in rc_pairs:
            this_ele = board[r][c]
            if this_ele not in element_counts or this_ele == ".":
                element_counts[this_ele] = 1
            else:
                return False
        
        if set(element_counts.keys()).issubset(valid_didgits):
            return True
        
        return False
    
    
    #gen rows to test
    rows_2_test = [[(x,y) for y in range(9)] for x in range(9)]
    
    #gen cols to test
    cols_2_test = [[(y,x) for y in range(9)] for x in range(9)]

    #gen the 9 squares
    corner_9 = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
    squares = []
    for x in range(0,9,3):
        for y in range(0,9,3):
            corner_transform = [(a+x,b+y) for a,b in corner_9]
            squares.append(corner_transform)
    
    all_tests = rows_2_test + cols_2_test + squares
    for i in squares: print(i)
    results = [check_element_range(x) for x in all_tests]
    print(results)
    return all(results)




print(isValidSudoku(board))














        