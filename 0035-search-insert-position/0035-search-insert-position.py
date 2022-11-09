class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        
        while right>=left:
            loc=(left+right)//2
            if nums[loc]==target:
                return loc
            if nums[loc]<target:
                left=loc+1
            else:
                right=loc-1

        return right+1