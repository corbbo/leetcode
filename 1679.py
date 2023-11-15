# You are given an integer array nums and an integer k.

# In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

# Return the maximum number of operations you can perform on the array.

class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        nums.sort()
        left, right, ops = 0, len(nums) - 1, 0
        while left < right:
            current_sum = nums[left] + nums[right]
            if current_sum == k:
                ops += 1
                left += 1
                right -= 1
            elif current_sum < k:
                left += 1
            else:
                right -= 1
        return ops