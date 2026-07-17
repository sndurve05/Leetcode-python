class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        list1=[]
        nums1.sort()
        nums2.sort()
        i=0
        j=0
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<nums2[j]:
                i+=1
            elif nums1[i]>nums2[j]:
                j+=1
            else:
                list1.append(nums1[i])
                i+=1
                j+=1
        list1=set(list1)
        list1=list(list1)

        return list1
    
#