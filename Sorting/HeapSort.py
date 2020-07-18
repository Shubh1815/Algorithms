def swap(arr, l, r):
    arr[l], arr[r] = arr[r], arr[l]


class Heap(object):
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)
        self.createHeap()
        
    def createHeap(self):
        for i in range(self.n // 2 , -1, -1):
            self.heapify(i)
        
    def heapify(self, i):
        while i < self.n // 2:
            l = i * 2 + 1
            r = i * 2 + 2

            if r < self.n and (self.arr[l] > self.arr[i] or self.arr[i] < self.arr[r]):
                if self.arr[l] >= self.arr[r]:
                    swap(self.arr, l, i)
                    i = i * 2 + 1
                else:
                    swap(self.arr, r, i)
                    i = i * 2 + 2
            elif self.arr[l] > self.arr[i]:
                swap(self.arr, l, i)
                i = i * 2 + 1
            else: 
                break

    def heapsort(self):
        while self.n > 0:
            self.heapify(0)
            swap(self.arr, 0, self.n - 1)
            self.n -= 1

    def __str__(self): 
        return str(self.arr)



arr = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]

arr = Heap(arr)
arr.heapsort()
print(arr)