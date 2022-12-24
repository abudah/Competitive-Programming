class Solution:
    def isPalindrome(self, s: str) -> bool:
        lists=''.join(item for item in s if item.isalnum()).lower()
        if lists==lists[::-1]:
            return True