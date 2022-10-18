class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer=[1]
        pre=1
        post=1
        for i in range(0,len(nums)-1):
            pre=pre*nums[i]
            answer.append(pre)
        for j in range(len(nums)-1,-1,-1):
            answer[j]= answer[j]*post
            post=post*nums[j]
        return answer