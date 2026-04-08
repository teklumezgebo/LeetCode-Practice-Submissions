class DynamicArray:
    
    def __init__(self, capacity: int):
        self.arr = []
        self.capacity = capacity

    def get(self, i: int) -> int:
        if len(self.arr) - 1 < i:
            print("Out of bounds")
            return 0
        else:
            return self.arr[i]

    def set(self, i: int, n: int) -> None:
        if len(self.arr) - 1 < i:
            print("Out of bounds")

        else:
            self.arr[i] = n
        
    def pushback(self, n: int) -> None:
        if len(self.arr) < self.capacity:
            self.arr.append(n)
        else:
            self.resize()
            self.arr.append(n)

    def popback(self) -> int:
        if len(self.arr) == 0:
            return 0
        else:
            return self.arr.pop()

    def resize(self) -> None:
        self.capacity *= 2

    def getSize(self) -> int:
        return len(self.arr)
    
    def getCapacity(self) -> int:
        return self.capacity