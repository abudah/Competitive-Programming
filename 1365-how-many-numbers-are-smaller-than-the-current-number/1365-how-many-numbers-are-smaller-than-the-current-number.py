class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        final=[]
        for i in nums:
            final.append(sorted(nums).index(i))
        return final