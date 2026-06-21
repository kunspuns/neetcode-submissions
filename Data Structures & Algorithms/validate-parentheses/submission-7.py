class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')':'(', '}':'{',']':'['}
        stack=[]

        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)

            elif not stack or pairs[char] != stack[-1]:
                return False

            else:
                stack.pop()

            
        return not stack
                

        