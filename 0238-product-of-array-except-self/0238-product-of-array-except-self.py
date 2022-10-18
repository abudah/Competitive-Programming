class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer=[]
        prefix=[nums[0]]
        postfix=[nums[-1]]
        for i in range(1,len(nums)):
            prefix.append(prefix[-1]*nums[i])
        for i in range(len(nums)-2,-1,-1):
            postfix.append(postfix[-1]*nums[i])
        postfix=postfix[::-1]
        for i in range(len(nums)):
            if i==0:
                answer.append(postfix[1])
            elif i==len(nums)-1:
                answer.append(prefix[len(nums)-2])
            else:
                answer.append(prefix[i-1]*postfix[i+1])
        return answer