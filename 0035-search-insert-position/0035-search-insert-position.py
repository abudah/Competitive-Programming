class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n=len(nums)
        if target in nums:
            return nums.index(target)
        for i in range(n):
            if nums[i]>target:
                return i
        return n