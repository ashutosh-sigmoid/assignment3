from functools import reduce
def lis_(arr, n):
    lis = [1 for i in range(n)]
    for i in range(1, n ):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[j] + 1 > lis[i]:
                lis[i] = lis[j] + 1

    maxi = 0


    maxi=reduce(lambda a,b:a if a>b else b,lis)

    return maxi


n = int(input())


a=[ int(item) for item  in input().split()]
res = lis_(a, n)

print(res)
