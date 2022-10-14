class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ans=count=0
        
        for i,c in enumerate(s):
            if i>=k:
                if s[i-k] in 'aeiou':
                    count-=1
            if c in 'aeiou':
                count+=1
            ans=max(ans,count)
        return ans
    