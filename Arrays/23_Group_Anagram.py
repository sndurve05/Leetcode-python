def groupAnagrams( strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        def anagram(s,t):
            if len(s)!=len(t):
                return False
            seen={}
            for char in s:
                if char in seen:
                    seen[char]+=1
                else:
                    seen[char]=1
            for char in t:
                if char in seen :
                    seen[char]-=1
            for val in seen.values():
                if val!=0:
                    return False
            return True

        hash_map={}
        for i in range (len(strs)-1):
            s = strs[i]
            for val in hash_map.values():
                if s not in val:
                    hash_map[s]=s
            print(hash_map)
            for j in (i+1,len(strs)):
                t = strs[j]
                print(s,t)
                if anagram(s,t):
                    hash_map[s]=hash_map[s] + t

        output=[]      
        for val in hash_map.values():
            output.append(tuple(val))

        return output

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))