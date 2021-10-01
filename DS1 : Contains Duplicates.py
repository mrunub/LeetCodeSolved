class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums)!=len(set(nums))
      
Success
Details 
Runtime: 181 ms, faster than 18.25% of Python3 online submissions for Contains Duplicate.
Memory Usage: 20 MB, less than 62.25% of Python3 online submissions for Contains Duplicate.
