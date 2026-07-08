# Traverse the array and increment count. 
# If the current index does not equal 1 (or n), 
# Take the maximum of 
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        res = 0
        for num in nums:
            if num == 1:
                count = count + 1
            else:
                 res = max(res, count)
                 count = 0
            res = max(res,count)
        return res