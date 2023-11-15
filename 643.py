# You are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        list_of_averages = []
        for i in range(len(nums)-k+1):
            list_of_averages.append(sum(nums[i:i+k])/k)
        return max(list_of_averages)