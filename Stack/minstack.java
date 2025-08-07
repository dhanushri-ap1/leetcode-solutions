import java.util.Stack;

class MinStack {

    private Stack<Integer> stk;
    private Stack<Integer> minStk;

import java.util.Stack

public MinStack() {
        stk = new Stack<>();
        minStk = new Stack<>();
    }

    public void push(int val) {
        stk.push(val);
        if (minStk.isEmpty() || val <= minStk.peek()) {
            minStk.push(val);
        }
    }

    public void pop() {
        int val = stk.pop();
        if (val == minStk.peek()) {
            minStk.pop();
        }
    }

    public int top() {
        return stk.peek();
    }

    public int getMin() {
        return minStk.peek();
    }
}





/*
Runtime: 5ms


In python: 
 class MinStack(object):

    def __init__(self):
        self.stk=[]
        self.min_stk=[]

    def push(self, val):
        self.stk.append(val) 
        if not self.min_stk or val<=self.min_stk[-1]:
            self.min_stk.append(val)
      
        

    def pop(self):
        val=self.stk.pop()
        if val==self.min_stk[-1]:
            self.min_stk.pop()

       
        

    def top(self):
        return self.stk[-1]
        

    def getMin(self):
        return self.min_stk[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

Runtime: 22ms





*/
  

