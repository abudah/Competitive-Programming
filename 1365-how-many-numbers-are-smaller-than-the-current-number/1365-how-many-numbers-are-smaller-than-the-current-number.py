class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        lists=[]
        for i in nums:
            lists.append(i)
        for i in range(len(nums)):
            for j in range(len(nums)-1):
                if nums[j]>=nums[j+1]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
        listing=[]
        for i in range(len(nums)):
            index=nums.index(lists[i])
            listing.append(index)
        return listing
    
            