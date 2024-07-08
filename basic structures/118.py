class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        if numRows == 0:
            return []
        
        resultado = [[1]]

        for i in range(numRows - 1):

            temporario = [0] + resultado[-1] + [0]
            linha = []

            for j in range(len(resultado[-1]) + 1):

                linha.append(temporario[j] + temporario[j + 1])
            
            resultado.append(linha)
            
        return resultado

