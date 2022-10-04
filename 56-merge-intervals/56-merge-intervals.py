class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        lists=[]
        for i in sorted(intervals,key=lambda i: i[0]):
            if lists and i[0] <= lists[-1][-1]:
                lists[-1][-1]=max(lists[-1][-1],i[1])
            else:
                lists+=[i]
        return lists
    
    