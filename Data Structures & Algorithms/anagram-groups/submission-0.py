class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tabela = {}

        for palavra in strs:
            chave_ordenada = "".join(sorted(palavra))

            if chave_ordenada not in tabela:
                tabela[chave_ordenada] = [palavra]
            else :
                tabela[chave_ordenada].append(palavra)

        res = []

        for el in tabela :
            res.append(tabela[el])

        return res

