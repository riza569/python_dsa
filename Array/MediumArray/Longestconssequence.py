def consseq(nums):
    #better approach
    # nums.sort()
    # n=len(nums)
    # max_cnt=1
    # cnt=1
    
    # for i in range(n-1):
    #     if nums[i]+1==nums[i+1]:
    #         cnt+=1
    #     elif nums[i]==nums[i+1]:
    #         continue
    #     else:
    #         max_cnt=max(max_cnt,cnt)
    #         cnt=1
    # max_cnt=max(max_cnt,cnt)        
    # return max_cnt
    
    #optimal
    
    n=len(nums)
    if n==0:
        return 0
    max_cnt=1
    st=set(nums)
    for it in st:
        if it-1 not in st:
            cnt=1
            x=it
            while x+1 in st:
                cnt+=1
                x+=1
            max_cnt=max(cnt,max_cnt)
    return max_cnt
arr=[3,8,5,7,6,5]
print(consseq(arr))