from functools import reduce
from operator import ixor
class Solution:
    def singleNumber(self, nums):
        return reduce(ixor, nums, 0)
