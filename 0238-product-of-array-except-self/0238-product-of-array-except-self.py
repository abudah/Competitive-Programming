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
           
        
        # for i in range(len(nums)-2,-1,-1):
        #     postfix.append(postfix[-1]*nums[i])
        # postfix=postfix[::-1]
        # for i in range(len(nums)):
        #     if i==0:
        #         answer.append(postfix[1])
        #     elif i==len(nums)-1:
        #         answer.append(prefix[len(nums)-2])
        #     else:
        #         answer.append(prefix[i-1]*postfix[i+1])
        return answer