# coding: utf-8

# 使用 deque 实现 栈

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


def test_stack():
    s = Stack()
    s.push(4)
    s.push(3)
    s.push(2)
    s.push(1)
    print(s.pop())
    print(s.pop())
    print(s.pop())


if __name__ == '__main__':
    test_stack()
