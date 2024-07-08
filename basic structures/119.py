class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        linha = [1]

        for i in range(1, rowIndex + 1):
            linha.append(linha[i - 1] * (rowIndex - i + 1) // i)
        
        return linha