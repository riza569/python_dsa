def kadane(nums):
    n=len(nums)
    # max_current_sum=0
    # for i in range(n):
    #     current_sum=0
    #     for j in range(i,n):
            
    #         current_sum+=nums[j]
     
    #         max_current_sum=max(current_sum,max_current_sum)
    # return max_current_sum
    
    if not nums:
        return 0
    max_sum=nums[0]
    current_sum=0
    ansstart,ansend=-1,-1
    start=0
    for i in range(n):
        if current_sum==0:
            start=i
            
        current_sum+=arr[i]
            
            
        if current_sum>max_sum:
            max_sum=current_sum
            ansstart=start
            ansend=i
            
        if current_sum<0:
            current_sum=0
            
    return [ansstart,ansend]    

arr=[-4,-3,-1]
print(kadane(arr))
