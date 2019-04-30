# coding: utf-8

# 堆就是完全二叉树
# 最大堆 父节点比孩子大

# topK 问题 大量元素找出 topK 固定内存
# 1. 前 K 个放入最小堆
# 2. 如果小于堆顶，pass
# 3. 如果大于堆顶，入堆，替换最小元素
import heapq
import random


class TopK:
    def __init__(self, array, k):
        self.min_heap = []
        self.capacity = k
        self.iterable = array

    def push(self, value):
        if len(self.min_heap) > self.capacity:
            heapq.heappushpop(self.min_heap, value)
        else:
            heapq.heappush(self.min_heap, value)

    def get_topk(self):
        for val in self.iterable:
            self.push(val)
        return self.min_heap


def test():
    ll = list(range(10000))
    random.shuffle(ll)
    print(ll)
    top = TopK(ll, 5)
    print(top.get_topk())


if __name__ == '__main__':
    test()
