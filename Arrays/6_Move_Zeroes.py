def moveZeroes(nums):
    j=-1
    for i in range(len(nums)):
        if nums[i]==0:
            j=i
            break
    i=j+1
    print ("i ",i,"j ",j)
    while i<len(nums) and j>=0:
        if nums[i]!=0:
            print(nums)
            nums[i],nums[j]=nums[j],nums[i]
            j+=1
            print(nums,j)
        i+=1
    return nums

print(moveZeroes([2,1]))