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
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        length = len(nums)
        fast = slow = 1
        while fast < length:
            if nums[fast] != nums[fast-1]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1

        return slow
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        fast = low = 2
        length = len(nums)
        while fast < length:
            if nums[fast] != nums[fast-2]:
                nums[low] = nums[fast]
                low += 1
            fast += 1
