def rearrange(nums):
    
    # n=len(nums)
    # neg_arr=[]
    # pos_arr=[]
    # neg_index=0
    # pos_index=0
    # for num in nums:
    #     if num<0:
    #         neg_arr.append(num)
            
    #     else:
    #         pos_arr.append(num)
            
    
    # for i in range(1,n,2):
    #     nums[i]=neg_arr[neg_index]
    #     neg_index+=1
        
    # for i in range(0,n,2):
    #     nums[i]=pos_arr[pos_index]
    #     pos_index+=1
    n=len(nums)
    pos_ind=0
    neg_ind=1
    arr=[0]*n
    for i in range(n):
        if nums[i]<0:
          arr[neg_ind]=nums[i]
          neg_ind+=2
          
        else:
            arr[pos_ind]=nums[i]
            pos_ind+=2
            
    return arr 
        
arr=[1,2,-3,-1,-2,3]
a=rearrange(arr)
print(a)