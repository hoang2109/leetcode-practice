# 290. Word Pattern

# Given a pattern and a string s, find if s follows the same pattern.
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

# Example 1:
# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true

# Example 2:
# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false

# Example 3:
# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false

# Example 4:
# Input: pattern = "abba", s = "dog dog dog dog"
# Output: false


class Solution(object):
    def wordPattern(self, pattern, s):
        mapping = {}
        words = s.split()

        if len(words) != len(pattern):
            return False

        for i in range(len(pattern)):
            if pattern[i] in mapping:
                if mapping[pattern[i]] != words[i]:
                    return False
            else:
                if words[i] in mapping.values():
                    return False
                else:
                    mapping[pattern[i]] = words[i]
        return True
