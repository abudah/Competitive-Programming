class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i=-1
        while len(s.split(' ')[i])==0:
            i-=1
        length=len(s.split(' ')[i])
        return length
    
        