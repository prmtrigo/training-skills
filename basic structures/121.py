class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        preco_minimo = prices[0]
        preco_maximo = 0

        for price in prices[1:]:
            preco_maximo = max(preco_maximo, price - preco_minimo)
            preco_minimo = min(preco_minimo, price)

        return preco_maximo