class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        occur={0:1}
        counter=0
        counterSum=0
        for i in nums:
            counterSum+=i
            if counterSum-k in occur:
                counter+=occur[counterSum-k]
            if counterSum in occur:
                occur[counterSum]+=1
            else:
                occur[counterSum]=1
        return counter