def bin(a,x):
    def helper(a,l,h,x):
        if h < l :
            return False
        mid = (l + h)//2
        if x > a[mid]:
            return helper(a,mid+1,h,x)
        elif x< a[mid]:
            return helper(a,l,mid-1,x)
        elif x == a[mid]:
            return True
    return helper(a,0,len(a)-1,x)
print(bin([5,7,9,11,13,15],5))
