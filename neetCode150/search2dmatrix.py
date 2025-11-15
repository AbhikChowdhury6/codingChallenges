from bisect import bisect_left
from types import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #first find which row it'll be in
        rownum = bisect_left(matrix, target, key=lambda x:x[0]) - 1
        print(rownum)

        if rownum != len(matrix)-1 and matrix[rownum + 1][0] == target:
            return True

        colnum = bisect_left(matrix[rownum], target)
        print(colnum)
        
        if colnum <= len(matrix[rownum])-1 and matrix[rownum][colnum] == target:
            return True
        return False