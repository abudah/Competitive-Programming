class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        coll={}
        for i in range(len(nums)):
            if nums[i] in coll:
                coll[nums[i]]+=1
            else:
                coll[nums[i]]=1
        
        for i in coll.values():
            if i>1:
                return True
        
