class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        numbers=sorted([int(i) for i in nums],reverse=True)
        return str(numbers[k-1])
        