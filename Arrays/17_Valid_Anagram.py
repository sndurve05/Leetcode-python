
def isAnagram( s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        seen ={}
        if len(s)!=len(t):
            return False

        for char in s:
            if char in seen:
                seen[char]+= 1
            else:
                seen[char] = 1

        for char1 in t:
            if char1 in seen:
                seen[char1] -= 1
      
        for values in seen.values():
            
            if values != 0:
                return False

        return True 
print(isAnagram("anagram","nagaram"))