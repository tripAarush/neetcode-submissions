class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # first binary search to find the row then binary search for val
        left = 0
        right = len(matrix)-1
        if not matrix[0]:
            return False

        row = -1
        while right >= left:
            mid = (right+left) // 2
            if target >= matrix[mid][0] and target <= matrix[mid][-1]:
                row = mid
                break
            elif target < matrix[mid][0]:
                right = mid-1
            else:
                left = mid+1
        
        if row == -1:
            return False
        
        left, right = 0, len(matrix[row])-1
        while right>=left:
            mid = (right+left) // 2
            if matrix[row][mid] == target:
                return True
            if matrix[row][mid] > target:
                right = mid-1
            else:
                left = mid + 1
        
        return False
