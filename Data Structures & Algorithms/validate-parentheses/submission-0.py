class Solution:
    def isValid(self, s: str) -> bool:
        pilha = []
        pares = {')': '(', ']': '[', '}': '{'}

        for c in s:
            if c in pares:
                if len(pilha) == 0:
                    return False
                if pilha[-1] == pares[c]:
                    pilha.pop()
                else:
                    return False
            else:
                pilha.append(c)

        if len(pilha) == 0:
            return True
        
        return False