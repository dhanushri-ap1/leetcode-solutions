class Solution(object):
    def searchMatrix(self, matrix, target):
            if not matrix or not matrix[0]:
                return False
            
            m,n=len(matrix),len(matrix[0]) #no or rows, no of columns
            low,high=0,m*n-1
      
            while low<=high:
                mid=(low+high)//2
                val=matrix[mid//n][mid%n]
                if val == target:
                    return True
                elif val<target:
                    low=mid+1
                else:
                    high=mid-1

            return False

if __name__ == "__main__":
    sol = Solution()
    print(sol.searchMatrix([[1,3,5],[7,9,11],[13,15,17]],13)) #A sample test case






'''
Leetcode problem: Search a 2D Matrix  
Runtime: 0 ms (Beats 100.00%), Memory: 13.40 MB (Beats 92.64%)  
Level: Medium  
Link: https://leetcode.com/problems/search-a-2d-matrix/

My Approach: The matrix is sorted such that each row is sorted left to right, and the first integer of each row 
is greater than the last integer of the previous row. So, we can treat the 2D matrix as a flattened 1D sorted array. 

We perform binary search on this virtual 1D array. Convert the 1D index to 2D using:
  - row = mid // number_of_columns
  - col = mid % number_of_columns

Compare the mid value with the target. If it's equal, return True.
If mid value is less than target, move the low pointer to mid + 1.
If it's greater, move the high pointer to mid - 1.

Continue this until the pointers cross. If not found, return False.

Time Complexity: O(log (m × n)), where m = number of rows, n = number of columns
'''
