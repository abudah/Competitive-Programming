class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=['']
        for i in s:
            if i=='(':
                stack.append('')
            elif i==')':
                add=stack.pop()
                stack[-1]+=add[::-1]
            else:
                stack[-1]+=i
        return stack[-1]