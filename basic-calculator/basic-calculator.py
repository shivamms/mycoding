class Solution:
    def ops(self,a,b,operator):
        if operator == "+":
            return a + b
        elif operator == "-":
            return a - b
        return 0

    def calculate(self,s: str) -> int:
        s = s.replace(" ","")
        stack = []
        operand = 0
        result = 0
        sign = 1
        for c in s:
            if c.isdigit():
                operand = (operand * 10) + int(c)
            elif c == "+":
                result += sign * operand
                sign = 1
                operand = 0
            elif c == "-":
                result += sign * operand
                sign = -1
                operand = 0
            elif c == "(":
                stack.append(result)
                stack.append(sign)
                sign = 1
                result = 0
            elif c == ")":
                result += sign * operand
                result *= stack.pop()
                result += stack.pop()
                operand = 0
        return result + sign * operand
            
        
        