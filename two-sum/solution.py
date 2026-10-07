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
        