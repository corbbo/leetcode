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
    
if __name__ == '__main__':
    solution = Solution()
    print(solution.maxOperations([1,2,3,4], 5)) # 2
    print(solution.maxOperations([3,1,3,4,3], 6)) # 1
    print(solution.maxOperations([2,2,2,3,1,1,4,1], 4)) # 2
    print(solution.maxOperations([5,1,3,4,7], 12)) # 1
    print(solution.maxOperations([1,1,1,2,2,2,4,4], 5)) # 2
    print(solution.maxOperations([1,1,1,2,2,2,4,4], 6)) # 2
    print(solution.maxOperations([1,1,1,2,2,2,4,4], 7)) # 0