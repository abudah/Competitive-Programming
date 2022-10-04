class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        sorted_nums=sorted(nums)
        n=len(sorted_nums)
        lists=[]
        for i in range(int(n/2)):
            lists.append((sorted_nums[i],sorted_nums[(n-1)-i]))
        final=[sum(i) for i in lists]
        return max(final)