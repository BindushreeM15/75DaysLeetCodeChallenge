class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count = {}  
        max_f = 0   
        left = 0
        res = 0
        
        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)
            
            max_f = max(max_f, count[s[right]])
            
           
            if (right - left + 1) - max_f > k:
                count[s[left]] -= 1
                left += 1
            
            res = max(res, right - left + 1)
            
        return res   