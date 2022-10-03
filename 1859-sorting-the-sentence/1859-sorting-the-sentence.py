class Solution:
    def sortSentence(self, s: str) -> str:
        s=s.split(" ")
        for i in range(len(s)):
            for j in range(len(s)-1):
                if s[j][-1]>s[j+1][-1]:
                    temp=s[j]
                    s[j]=s[j+1]
                    s[j+1]=temp
        for i in range(len(s)):
            s[i]=s[i][:-1]
        finalword=' '.join(str(x) for x in s)
        return finalword        