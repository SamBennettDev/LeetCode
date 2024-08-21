class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token.isdigit() or (token.startswith('-') and len(token) > 1):
                stack.append(int(token))
                continue

            op_2 = stack.pop()
            op_1 = stack.pop()

            if token == '+':
                res = op_1 + op_2

            elif token == '-':
                res = op_1 - op_2

            elif token == '*':
                res = op_1 * op_2

            elif token == '/':
                res = int(op_1 / op_2)

            stack.append(res)

        return stack[0]