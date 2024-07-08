class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        comeco = 0
        fim  = len(nums) -1

        while (comeco <= fim):

            meio = comeco + (fim - comeco) // 2

            if nums[meio] == target:
                return meio
            
            elif nums[meio] < target:
                comeco = meio + 1

            else:
                fim = meio - 1

        return comeco