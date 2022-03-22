class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = []
        for num in nums[:]:
            if num not in unique:
                unique.append(num)
            else: # num duplicated
                nums.remove(num)
        return len(nums)

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for n in range(len(nums)-1, 0, -1):
            if nums[n] == nums[n-1]:
                del nums[n]
        return len(nums)
