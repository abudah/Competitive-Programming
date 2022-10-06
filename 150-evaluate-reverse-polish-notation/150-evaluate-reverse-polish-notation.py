class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations=['+','-','*','/']
        stack=[]
        for i in tokens:
            if i in operations:
                
                second=int(stack.pop())
                first=int(stack.pop())
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