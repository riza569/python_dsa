def rearrange(nums):
    
    n=len(nums)
    neg_arr=[]
    pos_arr=[]
    neg_index=0
    pos_index=0
    for num in nums:
        if num<0:
            neg_arr.append(num)
            
        else:
            pos_arr.append(num)
            
    
    for i in range(1,n,2):
        nums[i]=neg_arr[neg_index]
        neg_index+=1
        
    for i in range(0,n,2):
        nums[i]=pos_arr[pos_index]
        pos_index+=1
        
arr=[1,2,-3,-1,-2,3]
rearrange(arr)
print(arr)