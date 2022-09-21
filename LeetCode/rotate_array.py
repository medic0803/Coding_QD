class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return 0
        # for i in range(0, k % len(nums)):
        #     nums.insert(0,nums.pop())
        length = len(nums)
        
        rotate = k%length
        if length == 1 or rotate == 0:
            return 0
        nums[:] = nums[-rotate:] + nums[:length-rotate]
# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         if k := (k % len(nums)):
#             nums[:k], nums[k:] = nums[-k:], nums[:-k]

