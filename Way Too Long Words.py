n = int(input())
for i in range(n):
    arr = input()
    l = len(arr)
    if l <= 10:
        print(arr)
    else:
        print(arr[0], l - 2, arr[-1], sep="")
