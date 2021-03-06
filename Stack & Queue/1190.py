# 1190. Reverse Substrings Between Each Pair of Parentheses

# You are given a string s that consists of lower case English letters and brackets.
# Reverse the strings in each pair of matching parentheses, starting from the innermost one.
# Your result should not contain any brackets.

# Example 1:
# Input: s = "(abcd)"
# Output: "dcba"

# Example 2:
# Input: s = "(u(love)i)"
# Output: "iloveu"
# Explanation: The substring "love" is reversed first, then the whole string is reversed.

# Example 3:
# Input: s = "(ed(et(oc))el)"
# Output: "leetcode"
# Explanation: First, we reverse the substring "oc", then "etco", and finally, the whole string.

# Example 4:
# Input: s = "a(bcdefghijkl(mno)p)q"
# Output: "apmnolkjihgfedcbq"


class Solution(object):
    def reverseParentheses(self, s):
        stack = ['']
        for c in s:
            if c == '(':
                stack.append('')
            elif c == ')':
                add = stack.pop()[::-1]
                stack[-1] += add
            else:
                stack[-1] += c
        return stack.pop()
