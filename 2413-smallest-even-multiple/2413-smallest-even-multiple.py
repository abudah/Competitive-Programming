class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        flag=False
        pos=1
        while flag==False:
            if pos%2==0 and pos%n==0:
                flag=True
                return pos        
            pos+=1
        