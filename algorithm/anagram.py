# coding: utf-8


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        char_list = [0] * 26
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            char_list[ord(s[i]) - 97] += 1
            char_list[ord(t[i]) - 97] -= 1
        for n in char_list:
            if n != 0:
                return False
        return True

