# 242. Valid Anagram
# Easy
# TopicsCompanies
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#  
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
# Input: s = "rat", t = "car"
# Output: false
#  
# Constraints:
# 1 <= s.length, t.length <= 5 * 10^4
# s and t consist of lowercase English letters.

#----------------------------------------------

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_s = {}
        count_t = {}

        for i in range (len(s)):
            count_s[s[i]] = count_s.get(s[i], 0) + 1
            count_t[t[i]] = count_t.get(t[i], 0) + 1

        return count_s == count_t

    
# if  s = "apple". The loop runs 5 times:

# 1. First letter ('a'): count_s.get('a', 0) returns 0. It adds 1. 
# Dictionary becomes {'a': 1}.

# 2. Second letter ('p'): count_s.get('p', 0) returns 0. It adds 1. 
# Dictionary becomes {'a': 1, 'p': 1}.

# 3. Third letter ('p'): count_s.get('p', 0) finds 'p' and returns 1. It adds 1. 
# Dictionary becomes {'a': 1, 'p': 2}.
