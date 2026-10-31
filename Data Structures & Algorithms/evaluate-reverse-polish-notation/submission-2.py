class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num=[]
        for i in tokens:
            if i not in ["+","-","*","/"]:
                num.append(int(i))
            else:
                b=num.pop()
                a=num.pop()

                if i == "+":
                    num.append(a+b)
                elif i == "*":
                    num.append(a*b)
                elif i == "-":
                    num.append(a-b)
                else:
                    num.append(int(a/b))
        return num[-1]                        

#DFS
        # def dfs():
        #     token = tokens.pop()
        #     if token not in "+-*/":
        #         return int(token)

        #     right = dfs()
        #     left = dfs()

        #     if token == '+':
        #         return left + right
        #     elif token == '-':
        #         return left - right
        #     elif token == '*':
        #         return left * right
        #     elif token == '/':
        #         return int(left / right)

        # return dfs()