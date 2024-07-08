class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        metade = len(nums) // 2
        root = TreeNode(nums[metade])
        root.left = self.sortedArrayToBST(nums[:metade])
        root.right = self.sortedArrayToBST(nums[metade+1:])
        return root
    