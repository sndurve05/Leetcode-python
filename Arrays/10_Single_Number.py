def fun(nums):
        nums.sort()
        print(nums)
        if len(nums)==1:
            return nums[0]
        for i in range(1,len(nums)-1):
            if nums[i]!=nums[i-1] and nums[i]!=nums[i+1]:
                print(nums[i])
                return nums[i]
        if nums[0]==nums[1]:
            return nums[-1]
        else:
           return nums[0]
            
print(fun([-336,513,-560,-481,-174,101,-997,40,-527,-336,513,-560,-481,-174,101,-997,40,-527,-784,-283,354]))