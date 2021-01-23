#https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        flag,numslen,ans=True,len(nums),[]
        for i in range(0,numslen):
            for j in range(0,numslen):
                if i != j:
                    if nums[i]+nums[j]==target:
                        ans=[i,j]
                        return ans
                        break
        
'''
Success
Details 
Runtime: 44 ms, faster than 85.48% of Python3 online submissions for Two Sum.
Memory Usage: 14.4 MB, less than 48.63% of Python3 online submissions for Two Sum.
'''
