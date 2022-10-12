class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
            start=0
            end=len(people)-1
            total=0
            people.sort()
            while start<=end:
                if people[start] + people[end]<=limit:
                    end-=1
                    start+=1
                else:
                    end-=1
                total+=1
            return total