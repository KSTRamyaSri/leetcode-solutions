class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
       # Guard clause: a pair cannot exist if there are fewer than 2 elements
        if not nums or len(nums) < 2:
            return []

        # Maps each number to its corresponding index: {value: index}
        seen = {}

        for current_index, num in enumerate(nums):
            complement = target - num

            # Check if the needed complement has already been traversed
            if complement in seen:
                return [seen[complement], current_index]

            # Cache the current number and its index for future lookups
            seen[num] = current_index

        # Fallback if no matching pair satisfies the condition
        return []