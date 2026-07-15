def merge(nums1, m, nums2, n, i=0, j=0):  
    for i ,j in zip(range(len(nums1),len(nums2))):

        if nums1[i]>=nums2[j]:
            nums1.insert(i,nums2[j])
            print(nums1)
    if j !=n :
        for j in range(len(nums2)):
            nums1[i].insert(i+1,nums2[j])      
    return nums1

print(merge([1,2,3,0,0,0],3,[2,5,6],3))