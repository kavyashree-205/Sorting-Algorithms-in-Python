def bubble_sort(a):
    n=len(a)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    return a

if __name__=="__main__":
    a=list(map(int,input().split()))
    print(bubble_sort(a))
