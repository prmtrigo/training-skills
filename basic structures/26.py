class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        resultado = 1

        for i in range (1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[resultado] = nums[i]
                resultado += 1
        
        return resultado