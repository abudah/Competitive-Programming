class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        strings= sorted(nums, key=lambda x:x/(10**len(str(x))-1),reverse=True)
        str_nums=[str(i) for i in strings]
        res=''.join(str_nums)
        res = str(int(res))
        return res
        
        