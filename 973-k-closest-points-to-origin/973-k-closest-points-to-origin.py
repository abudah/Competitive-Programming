class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return sorted(points, key=self.sorter)[:k]
    def sorter(self,item:List[int]):
            return sqrt(item[0]*item[0]+item[1]*item[1])     