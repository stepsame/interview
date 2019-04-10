# coding: utf-8


class Solution(object):
    f = [0, 1, 2]

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        first = 1
        second = 2
        for i in range(2, n):
            third = first + second
            first = second
            second = third
        return second

def test():
    s = Solution()
    print(s.climbStairs(3))


if __name__ == '__main__':
    test()
