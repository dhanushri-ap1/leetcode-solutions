class Solution(object):
    def clearDigits(self, s):
        d = []
        for c in s:
            if c.isdigit():
                d.pop()
            else:
                d.append(c)
        return ''.join(d)

if __name__ == "__main__":
    sol = Solution()
    print(sol.clearDigits("cb34")) #A sample test case








'''      
Leetcode problem: Clear digits
Runtime: 3 ms(Beats 47.78%), Memory: 12.36 (Beats 81.58%)
Level: Easy
Link: https://leetcode.com/problems/clear-digits/

My Approach: Use a stack and traverse the stack:
If c is a digit: pop the last element
Else: push c onto stack
Build result by joining the stack

Time Complexity: O(n)

'''
        
        
