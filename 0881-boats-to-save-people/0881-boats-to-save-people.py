class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
            start=0
            end=len(people)-1
            total=0
            sortedPeople=sorted(people)
            while start<=end:
                if sortedPeople[start] + sortedPeople[end]<=limit:
                    end-=1
                    start+=1
                else:
                    end-=1
                total+=1
            return total