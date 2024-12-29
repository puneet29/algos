class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        bracket_mapping = {"]": "[", "}": "{", ")": "("}
        for bracket in s:
            if bracket in ("(", "[", "{"):
                stack.append(bracket)
            else:
                if not stack:
                    return False
                popped_bracket = stack.pop()
                if popped_bracket != bracket_mapping[bracket]:
                    return False
        return True if stack == [] else False
