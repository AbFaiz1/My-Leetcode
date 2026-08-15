import heapq

class MedianFinder:

    def __init__(self):
        self.left = []    # max heap
        self.right = []   # min heap

    def addNum(self, num):

        if not self.right or num <= self.right[0]:
            heapq.heappush(self.left, -num)
        else:
            heapq.heappush(self.right, num)

        # Rebalance
        if len(self.left) > len(self.right) + 1:
            x = -heapq.heappop(self.left)
            heapq.heappush(self.right, x)

        elif len(self.right) > len(self.left):
            x = heapq.heappop(self.right)
            heapq.heappush(self.left, -x)

    def findMedian(self):

        if len(self.left) > len(self.right):
            return -self.left[0]

        return (-self.left[0] + self.right[0]) / 2