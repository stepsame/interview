# coding: utf-8


# 使用两个 队列 实现 栈
# 入栈 ： queue 1 直接入队
# 出栈 ： queue 1 出队，最后一个元素出队，其余元素 入队 queue 2，q1 q2 交换

from collections import deque


class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, x):
        self.items.append(x)

    def dequeue(self):
        return self.items.popleft()

    def empty(self):
        return len(self.items) == 0


class MyStack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x):
        self.q1.enqueue(x)

    def pop(self):
        while len(self.q1.items) > 1:
            self.q2.enqueue(self.q1.dequeue())
        x = self.q1.dequeue()
        self.q1, self.q2 = self.q2, self.q1
        return x

    def empty(self):
        return self.q1.empty()


def test_stack():
    s = MyStack()
    s.push(4)
    s.push(3)
    s.push(2)
    s.push(1)
    print(s.pop())
    print(s.pop())
    print(s.pop())

if __name__ == '__main__':
    test_stack()
