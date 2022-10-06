class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        length=len(nums2)
        for i in range(len(nums1)):
            n=nums2.index(nums1[i])
            Fgreater=-1
            for j in range(n,length):
                if nums2[j]>nums1[i]:
                    Fgreater=nums2[j]
                    break
            stack.append(Fgreater)
        return stack