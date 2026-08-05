## Two Sum
##You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

##You may assume that each input would have exactly one solution, and you may not use the same element twice.

##You can return the answer in any order.

##Example 1:

##Input: nums = [2,7,11,15], target = 9
##Output: [0,1]
##Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


#------------------------------------------------------------------
#solution 1 (slow)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]
        # Return an empty list if no solution is found
        return []
# O(n^2) time complexity, loop in a loop, slow nk mampus



#------------------------------------------------------------------

#solution 2 (fast)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        
        for i in range(len(nums)):
            current_number = nums[i]
            needed_number = target - current_number
            
            if needed_number in seen:
                return [seen[needed_number], i]
                
            # FIX: Write down the number we actually just saw
            seen[current_number] = i

# O(n) time complexity, O(n) space complexity, using a dictionary to store seen numbers and their indices, much faster than the first solution.