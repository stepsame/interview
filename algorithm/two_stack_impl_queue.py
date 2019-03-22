# coding: utf-8


# 使用两个 栈 实现 队列
# 入队 ： stack 1 的元素先全部 push 到 stack 2，新元素 push 到 stack 1，然后其他元素再 push 回来
# 出队 ： 直接 pop stack 1

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


class MyQueue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def enqueue(self, x):
        while not self.s1.empty():
            self.s2.push(self.s1.pop())
        self.s1.push(x)
        while not self.s2.empty():
            self.s1.push(self.s2.pop())

    def dequeue(self):
        return self.s1.pop()

    def empty(self):
        return self.s1.empty()


def test_queue():
    q = MyQueue()
    q.enqueue(4)
    q.enqueue(3)
    q.enqueue(2)
    q.enqueue(1)
    print(q.dequeue())
    print(q.dequeue())
    print(q.s1.items)


if __name__ == '__main__':
    test_queue()
