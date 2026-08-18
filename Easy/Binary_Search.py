# 704. Binary Search
# Easy
# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.
#  
# Example 1:
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
# Example 2:
# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1
#  
# Constraints:
# 1 <= nums.length <= 10^4
# -10^4 < nums[i], target < 10^4
# All the integers in nums are unique.
# nums is sorted in ascending order.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        # <= is important! If the array has only 1 element, left and right will be equal.
        while left <= right:
            # Calculate the middle index using integer division (//)
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            
            elif nums[mid] < target:
                # Target is bigger, so discard the left half
                left = mid + 1
                
            else:
                # Target is smaller, so discard the right half
                right = mid - 1
                
        # If the loop finishes and we haven't returned, the target isn't there
        return -1