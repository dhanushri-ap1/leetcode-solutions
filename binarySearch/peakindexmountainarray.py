class Solution(object):
    def peakIndexInMountainArray(self, arr):
        low=0
        high=len(arr)-1
        while low<high:
            mid=(low+high)//2
            if arr[mid]<arr[mid+1]:
                low=mid+1
            else:
                high=mid

        return low


if __name__ == "__main__":
    sol = Solution()
    print(sol.peakIndexInMountainArray([0,10,5,2])) #A sample test case
