class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        s=[i for i in range(1,n+1)]
        last=0
        while len(s)>1:
            last=(last+k-1)%len(s)
            del s[last]

        return s[0]
