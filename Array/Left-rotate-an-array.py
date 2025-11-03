def lefrotate(arr,k):
    
    l,r=0,len(arr)-1
    reverse(arr,l,r)
    reverse(arr,0,k-1)
    reverse(arr,k,len(arr)-1)
    
    
def reverse(arr,l,r) :
    while  l<r:
        arr[l],arr[r]=arr[r],arr[l]
        l+=1
        r-=1
        
        
arr=[1,2,3,4,5]
lefrotate(arr,3)
print(arr)