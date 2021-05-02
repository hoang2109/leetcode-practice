# 20. Valid Parentheses

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

# Example 4:
# Input: s = "([)]"
# Output: false

# Example 5:
# Input: s = "{[]}"
# Output: true


class Solution(object):
    def isValid(self, s):
        stack = []

        for ch in s:
            if ch == '(' or ch == '[' or ch == '{':
                stack.append(ch)
            elif ch == ')' and len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            elif ch == ']' and len(stack) > 0 and stack[-1] == '[':
                stack.pop()
            elif ch == '}' and len(stack) > 0 and stack[-1] == '{':
                stack.pop()
            else:
                return False

        return len(stack) == 0
