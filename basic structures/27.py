class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        contador = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[contador] = nums[i]
                contador += 1

        return contador