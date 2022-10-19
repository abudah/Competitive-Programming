import sys
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        countSum=0
        start=0
        length=sys.maxsize
        for i in range(len(nums)):
            countSum+=nums[i]
            while countSum>=target:
                length=min(length,i+1-start)
                countSum-=nums[start]
                start+=1
                
        if length==sys.maxsize:
            return 0
        else:
            return length 