# Given a binary array nums, return the maximum number of consecutive 1's in the array.
#
# ---------- Example -----------
##  Input: nums = [1,0,1,1,0,1]
##  Output: 2
# ------------------------------

from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        length = len(nums)
        max_length = 0
        counter = 0 
        for num in nums:
            if num == 0:
                if max_length < counter:
                    max_length = counter
                counter = 0
                continue        
            else:
                counter += 1
        else:
            if max_length < counter:
                max_length = counter
        return max_length
    