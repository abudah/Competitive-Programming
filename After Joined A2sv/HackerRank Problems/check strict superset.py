# Enter your code here. Read input from STDIN. Print output to STDOUT
setA=set(input().split())
n=int(input())
controlFlag=0
    
for l in range(n):
    setB=set(input().split())
    if len(setB)<len(setA) and setA.issuperset(setB):
        controlFlag+=1
if controlFlag!=n:
    print(False)
else:
    print(True)
