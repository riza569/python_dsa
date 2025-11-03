def subarray(arr,target):
    #Brute force
    # max_length=0
    # for i in range(len(arr)):
    #     sums=0
    #     for j in range(i,len(arr)):
    #         sums+=arr[j]
    #         if sums==target:
    #             current_length=j-i+1
                
    #             max_length=max(current_length,max_length)
                
    # return max_length
    # return max_sum
    
    
    
    #hashing
    # hashmap={}
    # sum=0
    # max_length=0
    
    # for i in range(len(arr)):
    #     sum+=arr[i]
        
    #     if sum==target:
    #         max_length=max(max_length,i+1)
            
        
    #     rem=sum-target
    #     if rem in hashmap:
    #         length=i-hashmap[rem]
    #         max_length=max(length,max_length)

    #     if sum not in hashmap:
    #         hashmap[sum]=i
        
    # return max_length     
    
    
    left=0
    right=0
    max_length=0
    sum=arr[left]
    n=len(arr)
    while right<n:
        while sum>target and left<=right:
            sum-=arr[left]
            left+=1
            
            
        if sum==target:
            max_length=max(max_length,right-left+1)  
             
        right+=1
        if right<n:
            sum+=arr[right]
            
        
    return max_length
    
arr=[2,3,5,1,1,2,3,3]
target=10
print(subarray(arr,target))