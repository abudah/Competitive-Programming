class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        dig=[str(i) for i in digits]
        digging=int("".join(dig))+1
        digg=[int(i) for i in str(digging)]
        return digg
        
        
        
        