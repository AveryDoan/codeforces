n=int(input())
result=0
for i in range(n):
    opi=input()
    if opi.count('1')>=2:
        result+=1
print(result)