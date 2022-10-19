class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        a,b=1,2
        for i in range(2,n):
            temp=b
            b=a+b
            a=temp
        return b