class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def squared(i):
            return i[0]**2 +i[1]**2
        return sorted(points, key=squared)[:k]
        