# You are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        list_of_averages = []
        for i in range(len(nums)-k+1):
            list_of_averages.append(sum(nums[i:i+k])/k)
        return max(list_of_averages)
    
if __name__ == '__main__':
    solution = Solution()
    print(solution.findMaxAverage([1,12,-5,-6,50,3], 4)) # 12.75
    print(solution.findMaxAverage([5], 1)) # 5.0
    print(solution.findMaxAverage([0,1,1,3,3], 4)) # 2.0
    print(solution.findMaxAverage([4,2,1,3,3], 2)) # 3.0
    print(solution.findMaxAverage([4,2,1,3,3], 3)) # 2.66667
    print(solution.findMaxAverage([9,7,3,5,6,2,0,8,1,9], 6)) # 6.16667
    print(solution.findMaxAverage([9,7,3,5,6,2,0,8,1,9], 3)) # 7.0
    print(solution.findMaxAverage([9,7,3,5,6,2,0,8,1,9], 1)) # 9.0
    print(solution.findMaxAverage([9,7,3,5,6,2,0,8,1,9], 2)) # 8.5
    print(solution.findMaxAverage([9,7,3,5,6,2,0,8,1,9], 4)) # 6.75
    print(solution.findMaxAverage([9,7,3,5,6,2,0,8,1,9], 5)) # 5.8
    print(solution.findMaxAverage([9,7,3,5,6,2,0,8,1,9], 7)) # 4.85714
    print(solution.findMaxAverage([9,7,3,5,6,2,0,8,1,9], 8)) # 4.625