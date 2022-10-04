class Solution:
    def largestNumber(self, nums: List[int]) -> str:
#         final=[]
#         for i in nums:
#             final.append(str(i))
        
                            
                  
#         return "".join(final)
        finalize=sorted(nums,key=lambda item:str(item))
        final=[]
        for i in finalize:
            final.append(str(i))

        for i in range(len(final)):
              for j in range(len(final)-1):    
                      if str(final[j])+str(final[j+1])<str(final[j+1])+str(final[j+1]):
                                final[j],final[j+1]=final[j+1],final[j]

        return "".join(final).lstrip('0') or '0'
        