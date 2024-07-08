class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        numeros = set()

        for i in nums:
            if i in numeros:
                return True
            else:
                numeros.add(i)
        
        return False