class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # An IP address string must be between 4 and 12 characters long
        if not s or len(s) < 4 or len(s) > 12:
            return []
            
        output = []
        
        def backtrack(start_idx, path):
            # Base case: if we have 4 segments and used the whole string
            if len(path) == 4:
                if start_idx == len(s):
                    output.append(".".join(path))
                return
            
            # Explore segments of length 1, 2, or 3
            for length in range(1, 4):
                # Ensure we don't go out of bounds
                if start_idx + length > len(s):
                    break
                    
                segment = s[start_idx : start_idx + length]
                
                # Check for leading zeros (e.g., "01" is invalid, but "0" is valid)
                if len(segment) > 1 and segment[0] == '0':
                    continue
                    
                # Check if the segment is a valid byte (0-255)
                if int(segment) <= 255:
                    backtrack(start_idx + length, path + [segment])

        backtrack(0, [])
        return output

# Test the solution
s = Solution()
# Note: Input must be wrapped in quotes as a string!
print(s.restoreIpAddresses("25525511135"))
