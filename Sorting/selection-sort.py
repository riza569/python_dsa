def selectionsort(arr):
    
    for i in range(len(arr)-1):
        
        
        min_ind=i
        
        for j in range(i+1,len(arr)):
            
            if arr[j]<arr[min_ind]:
                
                min_ind=j
                
            
        arr[i],arr[min_ind]=arr[min_ind],arr[i]
    
    
    
    
    
    
    
    
    
arr=[66,2,44,1,1,10]
selectionsort(arr)
print(arr)  