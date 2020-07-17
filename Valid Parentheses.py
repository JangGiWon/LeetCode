class Solution:
    def isValid(self, s: str) -> bool:
        b_list = list(s)
        answer = True
        stack = []

        for b in b_list:
            if b == '[' or b == '(' or s == '{':
                stack.append(b)
            elif len(stack) != 0:
                if(b == ']' and stack[-1] == '[') or (b == '}' and stack[-1] == '{') or (b == ')' and stack[-1] == '('):
                    stack.pop()
                else:
                    answer = False
                    break
            else:
                answer = False
                break
        
        if len(stack) != 0:
            answer = False

        return answer