def containsNearbyDuplicate(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        seen = {}          #key: nums[i] ; value : distance
        for n in range (len(nums)):
            if nums[n] not in seen:
                 seen[nums[n]]=0
            

        for key in seen:
            a = seen[key]
            key1 = key
            for key in seen :
                b = seen[key]
                key2 = key
                print(key1 , key2)
                print("a,b ",a,b)
                if a==b and abs(key1-key2)<=k and key1!=key2:
                    return True
        
        return False


print(containsNearbyDuplicate([1,2,3,1,2,3],2))