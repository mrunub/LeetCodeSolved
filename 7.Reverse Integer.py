#https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        rev=0
        if x in range(-(2**31),(2**31)):
            rev=int(str(abs(x))[::-1])
            if x<0:
                rev=-rev
            if abs(rev) not in range(0,(2**31)):
                return 0
        return rev
        
'''

Success
Details 
Runtime: 28 ms, faster than 88.97% of Python3 online submissions for Reverse Integer.
Memory Usage: 14.1 MB, less than 71.84% of Python3 online submissions for Reverse Integer.

'''
