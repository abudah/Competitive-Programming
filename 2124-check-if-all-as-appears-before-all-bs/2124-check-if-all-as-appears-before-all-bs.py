class Solution:
    def checkString(self, s: str) -> bool:
        first=s
        second=''.join(sorted(s))
        if first==second:
            return True