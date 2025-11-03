def twosum(arr,target):
    
    # n=len(arr)
    # for i in range(n):
        
    #     for j in range(i,n):
    #         if arr[i]+arr[j]==target:
    #             return [i,j]
            
    # return [-1,-1]
    
    n=len(arr)
    hashmap={}
    for i in range(n):
        rem=target-arr[i]
        
        if rem in hashmap:
            return[hashmap[rem],i]
            
        hashmap[arr[i]]=i
        
    return [-1,-1]
    
    # arr.sort()
    # l,r=0,len(arr)-1
    # while l<r:
        
    #     sum=arr[l]+arr[r]
    #     if sum==target:
    #         return[l,r]
        
    #     elif sum>target:
    #         r-=1
        
    #     else:
    #         l+=1
            
    # return[-1,-1]
    
arr=[2,6,5,8,11]
target=14
print(twosum(arr,target))