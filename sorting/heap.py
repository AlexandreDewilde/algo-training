import random
class Heap:

    def __init__(self):
        self.array = []
    
    def insert(self, val):
        self.array.append(val)
        self.swim(len(self.array)-1)

    def swim(self, pos):
        if pos and self.array[pos] < self.array[pos//2]:
            self.array[pos], self.array[pos//2] = self.array[pos//2], self.array[pos]
            self.swim(pos//2)
    
    def sink(self, pos):
        smallest = pos
        if len(self.array) > pos*2 and self.array[pos*2] < self.array[smallest]:
            smallest = pos*2
        if len(self.array) > pos*2+1 and self.array[pos*2+1] < self.array[smallest]:
            smallest = pos*2+1
        if self.array[smallest] < self.array[pos]:
            self.array[smallest], self.array[pos] = self.array[pos], self.array[smallest]
            self.sink(smallest)
            
    def poll(self):
        if len(self.array) == 1:
            return self.array.pop()
        val = self.array[0]
        self.array[0] = self.array.pop()
        self.sink(0)
        return val

        

if __name__ == "__main__":
    pq = Heap()

    for _ in range(10):
        pq.insert(random.randrange(100))
    
    while len(pq.array):
        print(pq.poll())