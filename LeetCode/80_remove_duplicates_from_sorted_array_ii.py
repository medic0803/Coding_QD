class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        fast = slow = 2
        length = len(nums)
        while fast < length:
            if nums[fast] != nums[slow - 2]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        def expand(duplicates: int):
            fast = slow = duplicates
            length = len(nums)
            while fast < length:
                if nums[fast] != nums[slow - duplicates]:
                    nums[slow] = nums[fast]
                    slow += 1
                fast += 1
            return slow
        return expand(2)
