class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        deq = []
        total = 0
        for item in tokens:
            if item not in "+-/*":
                deq.append(int(item))
            else:
                if item == "+":
                    deq.append(deq.pop() + deq.pop())
                elif item == "-":
                    s = deq.pop()
                    f = deq.pop()
                    deq.append(f-s)
                elif item == "*":
                    deq.append(deq.pop() * deq.pop())
                else: 
                    s = deq.pop()
                    f = deq.pop()
                    deq.append(int(float(f)/s))
        return deq.pop()