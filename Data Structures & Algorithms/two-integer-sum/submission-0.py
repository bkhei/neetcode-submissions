# Iterate over the array, subtract the target from the current element
# Check to see if the array has the desired difference, and return that index

# For each value in the array (keep track w/ i and n)
# We set the difference as the target - current element
# If that difference is in the hashmap that we are iterating over
# Return the difference alongside the index
# Set the hashMap at that index to the current one
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, n in enumerate(nums): 
            diff = target - n 
            if diff in hashmap:
                return [hashmap[diff], i] 
            hashmap[n] = i 