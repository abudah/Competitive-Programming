#User function Template for python3

class Solution: 
    def select(self, arr, i):
        minimumIndex=i
        for n in range(i+1,len(arr)):
                if arr[n]<arr[minimumIndex]:
                    minimumIndex=n
        return minimumIndex
        
        # code here 
    
    def selectionSort(self, arr,n):
        for i in range(len(arr)-1):
            minPos=self.select(arr,i)
            temp=arr[i]
            arr[i]=arr[minPos]
            arr[minPos]=temp

        #code here
