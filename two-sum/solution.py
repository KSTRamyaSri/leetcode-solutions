class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
       #hi
       #hi
       #hiiiiiiiiiiiiiiii

        hashmap = {} #hashmap

        for i, num in enumerate(nums): 
            complement = target - num

            if complement in hashmap:
                return [hashmap[complement], i] #returning

            hashmap[num] = i
        