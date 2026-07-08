# Given an array of numbers
# If the number appears more than once, return true
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        array = set()
        for number in nums:
            if number in array:
                return True
            array.add(number)
        return False