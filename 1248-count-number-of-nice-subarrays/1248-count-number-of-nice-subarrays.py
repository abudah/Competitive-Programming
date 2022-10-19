class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int: 
        for i in range(len(nums)):
            nums[i]=nums[i]%2
        count=0
        countSum=0
        coll={0:1}
        for i in range(len(nums)):
            countSum+=nums[i]
            if countSum-k in coll:
                count+=coll[countSum-k]
            if countSum in coll:
                coll[countSum]+=1
            else:
                coll[countSum]=1
        return count