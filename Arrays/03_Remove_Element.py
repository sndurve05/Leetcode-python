def removeElement(nums, val ,j=0):
    for i in range (len(nums)):
        
        if nums[i]!=val:
            nums[j]=nums[i]
            j+=1

    return (j,nums)

print(removeElement([0,1,2,2,3,0,4,2],2))