class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        good=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] == nums[j] and i < j:
                    good+=1
        return good