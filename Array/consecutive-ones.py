def consecutive(arr):
    cnt=0
    max_cnt=0
    for i in range(len(arr)-1):
        
        if arr[i]==1:
            cnt+=1

        else:
            cnt=0
        max_cnt=max(cnt,max_cnt)
     
    return max_cnt
    
    
    
arr=[1,0,0,1,1,1,1,1,1,0,0,1,1,1,1,0,0,1,1,1,1,1,1,1,1]
print(consecutive(arr))