class SinglyLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def __contains__(self, target):
        curNode = self._head
        while curNode is not None and curNode.item != target:
            curNode = curNode.next
        return curNode is not None

    def add(self, item):
        newNode = _SinglyListNode(item)
        if self._head is None:
            self._head = newNode
        else:
            self._tail.next = newNode
        self._tail = newNode
        self._size += 1

    def remove(self, item):
        predNode = None
        curNode = self._head
        while curNode is not None and curNode.item != item:
            predNode = curNode
            curNode = curNode.next
        assert curNode is not None, "The item must be in the bag!"
        self._size -= 1
        if curNode is not None:
            if curNode is self._head:
                head = curNode.next
            else:
                predNode.next = curNode.next
            if curNode is self._tail:
                self._tail = predNode
        return curNode.item

    def __iter__(self):
        return _SinglyIterator(self._head)

class _SinglyListNode(object):
    def __init__(self, item):
        self.item = item
        self.next = None

class _SinglyIterator:
    def __init__(self, listHead):
        self._curNode = listHead

    def __iter__(self):
        return self

    def __next__(self):
        if self._curNode is None:
            raise StopIteration
        else:
            item = self._curNode.item
            self._curNode = self._curNode.next
            return item

    def next(self):
        return self.__next__()


if __name__=="__main__":
    listA = SinglyLinkedList()
    listA.add('a')
    listA.add('b')
    listA.add('c')
    listA.add('d')
    listA.remove('c')

    for item in listA:
        print(item)