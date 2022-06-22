n=int(input())
arr=[]
for i in range (n):
    arr.append(input())

def ans(arr):
    for j in range(len(arr)):
        if len(arr[j])>=10:
            temp=arr[j]

            arr[j]=temp[0]+str(len(temp[1:-1]))+temp[-1]
    
    return arr

print(ans(arr))
