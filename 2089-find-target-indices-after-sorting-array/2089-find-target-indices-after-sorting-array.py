class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        index,count=0,0
        for i in nums:
            if i<target:
                index+=1
            elif i==target:
                count+=1
                
        return range(index,index+count)