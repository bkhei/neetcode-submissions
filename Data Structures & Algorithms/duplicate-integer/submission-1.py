# For each number in the array
# Return true if it appears more than once, false if it does not
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
      stored = set()
      for i in nums:
        if i in stored:
          return True
        stored.add(i)
      return False
