def containsNearbyDuplicate(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        seen = {}
        for n in range (len(nums)):
            seen[n]=nums[n]
        print(seen)
        for key in seen:
            if key+k>=len(seen):
                return False
            a=seen[key]
            b=seen[(key+k)]
            print(a,b)
            if a==b:
                return True

    

print(containsNearbyDuplicate([1,2,3,1,2,3],3))