class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
       

        hashmap = {} #hashmap

        for i, num in enumerate(nums): #forloop
            complement = target - num

            if complement in hashmap:
                return [hashmap[complement], i] #returning

            hashmap[num] = i
        