def numbers_twice(arr):
    
    # hashs={}
    # for num in arr:
    #     hashs[num]=hashs.get(num,0)+1
    
    # for key,value in hashs.items():
    #     if value==1:
    #         return key
    
    missing=0
    for num in arr:
        missing^=num
    return missing
    
arr=[4,1,2,1,2,4,3]
print(numbers_twice(arr))