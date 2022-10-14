class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        subsum=sum(arr[:k])
        numSub=0
        if int(subsum/k)>=threshold:
                numSub+=1
        for i in range(1,len(arr)-k+1):
            subsum=subsum-arr[i-1]
            subsum=subsum+arr[i+k-1]
            if int(subsum/k)>=threshold:
                numSub+=1
    
        return numSub
        