# coding: utf-8

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        mask = 1
        bits = 0
        for _ in range(32):
            if n & mask != 0:
                bits += 1
            mask <<= 1
        return bits