class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l , r = 0, len(matrix) - 1
        target_list = None

        while l <= r:
            m = (r + l) // 2

            if matrix[m][0] <= target <= matrix[m][-1]:
                target_list = matrix[m]
                break 
            
            elif matrix[m][0] > target:
                r = m - 1
            
            else:
                l = m + 1
        
        if not target_list:
            return False

        l , r = 0, len(target_list) - 1

        while l <= r:
            m = (r + l) // 2

            if target_list[m] == target:
                return True 
            
            elif target_list[m] > target:
                r = m - 1
            
            else:
                l = m + 1
        
        return False
            

        
    





