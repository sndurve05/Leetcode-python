def removeDuplicates(nums ,i=0):
        
    for j in range(i+1,len(nums)):
        print(i,nums)
        num1=nums[i]
        num2=nums[j]
        print("i: ",i,"\nj: ",j,"\nnum1,num2: ",num1,num2)
        if num1!=num2:
            nums[i+1]=num2
            i+=1
    return (i+1,nums)

print(removeDuplicates([0,0,0,0,1]))