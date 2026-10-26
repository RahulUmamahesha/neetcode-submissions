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
