class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        len0 = 0
        len1 = 0
        c0= ""
        c1=""
        for i in s:
            if i =='1':
                c1+="1"
                len0 = max(len(c0),len0)
                c0 = ""
            else:
                c0 += "0"
                len1 = max(len(c1),len1)
                c1=""
        len0 = max(len(c0),len0)
        len1 = max(len(c1),len1)
        
        return len1 > len0 