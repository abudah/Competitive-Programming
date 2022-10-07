class NumArray:

    def __init__(self, nums: List[int]):
        self.nums=nums
        self.prefix_nums=[0]
        for num in nums:
            self.prefix_nums+=[self.prefix_nums[-1]+num]

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_nums[right+1]-self.prefix_nums[left]
    

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)