def buystoc(nums):
    
    # n=len(nums)
    # curr_sum=0
    # max_sum=0
    # for i in range(n):
        
    #     for j in range(i+1,n):
    #         if nums[j]>nums[i]:
    #             curr_sum=nums[j]-nums[i]
            
    #             max_sum=max(curr_sum,max_sum)
            
            
    # return max_sum
    l,r=0,1
    n=len(nums)
    max_profit=0
    while r<n:
        
        if nums[r]-nums[l]<0:
            l=r     
        else:
            profit=nums[r]-nums[l]
            max_profit=max(max_profit,profit)

        r+=1
    return max_profit
arr=[7,1,5,3,6,4]
print(buystoc(arr))