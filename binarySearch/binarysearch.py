class Solution(object):
    def search(self, nums, target):
        low=0
        high=len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                return mid
            elif  nums[mid]<target:
                low=mid+1
            else:
                high=mid-1

        return -1

if __name__ == "__main__":
    sol = Solution()
    print(sol.search([3,4,5,6,8,9,10,23,25], 10)) #A sample test case
               


'''
Leetcode problem: Binary Search
Runtime: 0 ms(Beats 100.00%), Memory: 13.30 (Beats 92.64%)
Level: Easy
Link: https://leetcode.com/problems/binary-search

My Approach: First take a sorted array, Use two pointers, one low pointer at the beginning of the array
and one pointer at the end of the array called high. Mid=(low+high)//2

Check if the element to be found is at the middle. Else check if middle element is lesser than target. Then check for
the element in right half by doing low=mid+1. Else if middle element is greater than target, check for element
in left half by doing high=mid-1. Continuously split the array until element is found and find mid and respective
left and right halves. Return index of found element.

Time Complexity: O(log n)
'''
