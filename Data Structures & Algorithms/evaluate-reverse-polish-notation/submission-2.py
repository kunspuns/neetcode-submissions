class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]

        for char in tokens:
            if char not in ['+','-','*','/']:
                stack.append(int(char))

            else:
                b=stack.pop()
                a=stack.pop()

                if char == '-':
                    stack.append(a - b)
                if char == '+':
                    stack.append(a + b)
                if char == '/':
                    stack.append(int(a / b))
                if char == '*':
                    stack.append(a * b)

        return stack.pop()
        