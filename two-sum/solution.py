class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
      

        hashmap = {} # Maps each number to its corresponding index: {value: index}

        for i, num in enumerate(nums):  #forloop
            complement = target - num

            # Check if the needed complement has already been traversed
            if complement in hashmap:
                return [hashmap[complement], i] #returning
            # Cache the current number and its index for future lookups
            hashmap[num] = i



# ============================================================
# Approach 2 — New Approach
# Added: 07 October 2026
# ============================================================


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Pair each number with its original index and sort by value
        indexed_nums = sorted(enumerate(nums), key=lambda x: x[1])
        
        left = 0
        right = len(nums) - 1
        
        while left < right:
            current_sum = indexed_nums[left][1] + indexed_nums[right][1]
            
            if current_sum == target:
                return [indexed_nums[left][0], indexed_nums[right][0]]
            elif current_sum < target:
                left += 1   # Increase sum by moving left pointer rightward
            else:
                right -= 1  # Decrease sum by moving right pointer leftward
                
        return []
