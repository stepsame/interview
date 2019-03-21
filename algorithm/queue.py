# coding: utf-8

# 使用 deque 实现 队列

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


def test_queue():
    q = Queue()
    q.enqueue(4)
    q.enqueue(3)
    q.enqueue(2)
    q.enqueue(1)
    print(q.dequeue())
    print(q.dequeue())
    print(q.items)


if __name__ == '__main__':
    test_queue()
