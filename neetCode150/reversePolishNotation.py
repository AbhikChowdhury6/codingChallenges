from types import List
#A2
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [int(tokens.pop(0))]
        while len(tokens) > 0:
            #print(stack)
            next_token = tokens.pop(0)
            try:
                stack.append(int(next_token))
                continue
            except:
                pass
            

            op = next_token
            right = stack.pop()
            left = stack.pop()
            #print(left, op, right, stack)
            

            if op == "+":
                stack.append(left + right)
            if op == "-":
                stack.append(left - right)
            if op == "*":
                stack.append(left * right)
            if op == "/":
                if left < 0 or right < 0:
                    out = (left * -1) // right
                    stack.append(-1 * out)
                else:
                    stack.append(left // right)   

        return stack[0] 

#10 6 9 3 + -11 * / * 17 + 5 +
            


#A1
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def prep(left):
            next_op = left.pop()
            next_right = int(left.pop())
            return [left, next_right, next_op]
        
        def operate (left: list[str], right: int, op: str):
            #print(left, right, op)
            if len(left) == 1:
                l = int(left[0])
            else:
                l = operate(*prep(left))
            #print(l)
            if op == "+":
                return l + right
            elif op == "-":
                return l - right
            elif op == "*":
                return l * right
            elif op == "/":
                return l // right
        
        return operate(*prep(tokens))