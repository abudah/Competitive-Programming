class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        start=0
        for i in t:
            if i==s[start]:
                start+=1
                if start==len(s):
                    return True
        return False