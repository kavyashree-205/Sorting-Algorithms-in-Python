def insertion_sort(a):
    n=len(a)
    for i in range(1,n):
        current_element=a[i]
        j=i-1
        while current_element<a[j] and j>=0:
            a[j+1]=a[j]
            j=j-1
        a[j+1]=current_element
    return a
if __name__=="__main__":
    a=[int(x) for x  in input().split()]
    print(insertion_sort(a))
