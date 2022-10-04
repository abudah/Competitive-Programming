class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n=int(len(nums)/2)
        lists=[]
        for i in range(n):
            lists.append((nums[i],nums[(n*2-1)-i]))
        return max([sum(i) for i in lists])