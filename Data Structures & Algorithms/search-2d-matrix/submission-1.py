class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n=len(matrix),len(matrix[0])
        row,ele = 0,n-1
        while row<m and ele >= 0:
            if matrix[row][ele] > target:
                ele -= 1
            elif matrix[row][ele] < target:
                row += 1    
            else:
                return True
        return False       
               
             
        

      

                 