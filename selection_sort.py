def selection_sort(a):
    for i in range(0,n-1):
        minimum_index=i
        for j in range(i+1,n):
            if a[j]<a[minimum_index]:
                minimum_index=j
        a[i],a[minimum_index]=a[minimum_index],a[i]
    return a

if __name__=="__main__":
    a=list(map(int,input().split()))
    n=len(a)
    print(selection_sort(a))
    
