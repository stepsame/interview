# coding: utf-8

# 最小值栈
# 思路一： 两个栈，一个存当前最小值，如果出栈当前最小值一起出
# 思路二： 一个栈，每次入栈当前最小值也入栈，出栈时最小值出两次

from collections import deque


class Stack:
    def __init__(self):
        self.items = deque()

    def push(self, x):
        self.items.append(x)

    def pop(self):
        return self.items.pop()

    def empty(self):
        return len(self.items) == 0


class MinStack:
    def __init__(self):
        self.s = Stack()
        self.min_stack = Stack()

    def push(self, x):
        if self.min_stack.empty():
            self.min_stack.push(x)
        else:
            min_value = self.min_stack.items[-1]
            if min_value > x:
                self.min_stack.push(x)

        self.s.push(x)

    def pop(self):
        val = self.s.pop()
        if not self.min_stack.empty():
            min_value = self.min_stack.items[-1]
            if val == min_value:
                self.min_stack.pop()
        return val

    def get_min(self):
        return self.min_stack.items[-1] if not self.min_stack.empty() else None


def test_stack():
    s = MinStack()
    s.push(4)
    s.push(8)
    s.push(3)
    s.push(5)
    print(s.get_min())
    s.pop()
    print(s.get_min())
    s.pop()
    print(s.get_min())
    s.pop()
    print(s.get_min())
    s.pop()
    print(s.get_min())


if __name__ == '__main__':
    test_stack()
