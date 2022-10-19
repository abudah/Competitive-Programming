class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack, ans = [], dict.fromkeys(nums2, -1)
        for i, n in enumerate(nums2):
                while stack and stack[-1] < n:
                    ans[stack.pop()] = n
                stack += n,

        return map(ans.get, nums1)