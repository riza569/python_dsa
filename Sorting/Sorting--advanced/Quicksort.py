def quicksort(arr,low,high):
    if low<high:
        
        pivot=partition(arr,low,high)
        quicksort(arr,low,pivot-1)
        quicksort(arr,pivot+1,high)
        
        
        
def partition(arr,low,high):
    
    pivot=arr[low]
    i=low
    j=high
    
    while i<j:
        
        while i<=high and arr[i]<=pivot:
            i+=1
            
        while j>=low and arr[j]>pivot:
            j-=1
            
        if i<j:
            
            arr[i],arr[j]=arr[j],arr[i]
            
    arr[j],arr[low]=arr[low],arr[j]
    
    
    return j


arr=[66,2,44,1,10]
quicksort(arr,0,len(arr)-1)
print(arr)