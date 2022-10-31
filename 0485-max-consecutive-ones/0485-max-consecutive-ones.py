class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cons=0
        con=''
        for i in nums:
            if i==1:
                con+='1'
            else:
                cons=max(len(con),cons)
                con=''
        cons=max(len(con),cons)
        return cons