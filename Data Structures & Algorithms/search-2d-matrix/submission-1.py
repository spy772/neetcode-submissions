class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        check = []
        for row in matrix:
            if row[-1] >= target:
                check = row
                break
        
        for col in check:
            if col == target:
                return True
        
        return False