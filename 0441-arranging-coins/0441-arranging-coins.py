class Solution:
    def arrangeCoins(self, n: int) -> int:
        i=0
        while n>0:
            i+=1
            n-=i
        if n==0:
            return i
        else:
            return i-1