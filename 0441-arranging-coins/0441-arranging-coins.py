class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n==1:
            return 1
        i=1
        sum=0
        while True:
            sum=int(i*(i+1)/2)
            if sum>n:
                break
            i+=1
        return i-1