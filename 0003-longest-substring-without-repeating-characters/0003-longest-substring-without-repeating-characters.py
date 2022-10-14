class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        result=0
        subSet=set()
        for right in range(len(s)):
            while s[right] in subSet:
                subSet.remove(s[left])
                left+=1
            subSet.add(s[right])
            result=max(result,right-left+1)
        return result