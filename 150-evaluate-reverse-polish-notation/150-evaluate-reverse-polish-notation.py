class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i in ['+','-','*','/']:
                second,first=int(stack.pop()),int(stack.pop())
                operate=0
                if i=='*':
                    operate=int(first*second)    
                elif i=="/":
                    operate=int(first/second)
                elif i=="+":
                    operate=first+second
                else:
                    operate=first-second
                stack.append(operate)
                
            else:
                stack.append(i)
        return stack[-1]