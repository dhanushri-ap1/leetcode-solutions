class Solution(object):
    def isValid(self, s):
        stk=[]
        dict={')': '(','}':'{',']':'['}
        for i in s:
            if i in '({[':
                stk.append(i)
            if i in ']})':
                if not stk or stk[-1]!=dict[i]:
                    return False
                stk.pop()

        return len(stk)==0


'''
Time complexity: 0(n)
Runtime : 0ms
Approach: just use basic string operations. Take an empty stack. Loop through the string, if i in '({[', then append to stack. if i in ')}]', and if 
top of stack is not part of dictionary, return invalid. else pop. Then return true if stack is empty


'''
