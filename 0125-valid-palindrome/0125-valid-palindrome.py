class Solution(object):
    def isPalindrome(self, s):
        new = ''.join(ch.lower() for ch in s if ch.isalnum())
        return new == new[::-1]

        
        