#Queue ADT using Python list
class Queue:
    def __init__(self):
        self._qList = list()

    def isEmpty(self):
        return len(self) == 0

    def __len__(self):
        return len(self._qList)

    def enqueue(self, item):
        self._qList.append(item)

    def dequeue(self):
        assert not self.isEmpty(), "Queue is empty"
        self._qList.pop(0)
    def printQueue(self):
        print(self._qList)

Q=Queue()
for i in range(10):
    Q.enqueue(i)
Q.printQueue()
Q.dequeue()
Q.printQueue()
Q.dequeue()
Q.printQueue()