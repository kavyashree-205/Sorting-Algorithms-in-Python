def partition(a,low,high):
    pivot=a[low]
    i=low+1
    j=high
    while True:
        while i<=j and a[i]<=pivot:
            i=i+1
        while i<=j and a[j]>=pivot:
            j=j-1
        if i<j:
            a[i],a[j]=a[j],a[i]
        else:
            break
    a[low],a[j]=a[j],a[low]
    return j
    
def quick_sort(a,low,high):
    if low<high:
        partition_index=partition(a,low,high)
        quick_sort(a,low, partition_index-1)
        quick_sort(a, partition_index+1,high)

if __name__=="__main__":
    a=list(map(int,input().split()))
    n=len(a)
    quick_sort(a,0,n-1)
    print(a)
