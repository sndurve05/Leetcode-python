class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        s = s.split(" ")
        map={}
        if len(pattern)!= len(s):
            return False
        for char,word in zip(pattern,s):
            if char not in map and word not in map.values():
                map[char]=word
                
            elif char in map and word in map.values():
                  if map[char]!=word:
                        return False

            elif (char in map or word in map.values()) :
                    return False

        return True