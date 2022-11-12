class Solution:
    def sortSentence(self, s: str) -> str:
        def take_end(elem):
            return elem[-1]
        p=sorted(s.split(), key=take_end )
        c=p[0][:-1]
        for i in range(1,len(p)):
            c+=' '+p[i][:-1]
        return c
            