# Python3 Program to flatten list with
# next and child pointers

# A linked list node has data,
# next pointer and child pointer
from termcolor import colored
from colorama import Fore, Style
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.child = None

class multiLevelLinkedList():
    def __init__(self):
        self._head=None
        self._size=0

    def traverseNext(self, Node,data):
        curNode = Node
        while (curNode != None):
            if curNode.data==data:
                return nextlink, True
            nextlink = curNode
            curNode = curNode.next
        return nextlink, False

    def traverseChild(self, Node):
        curNode = Node
        while (curNode != None):
            nextchild = curNode
            curNode = curNode.child
        return nextchild


    def createNode(self,data):
        duplicate = False
        if self._head==None:
            self._head=Node(data)
            self._size += 1
        else:
            curNode=self._head
            newNode, duplicate= self.traverseNext(curNode,data)
            if duplicate == True:
                print (Fore.RED+'item already exist, can not add into the list'+Style.RESET_ALL)
                return
            else:
                newNode.next=Node(data)
                self._size += 1

    def __len__(self):
        return self._size

    def createChild(self,parent,child):
        isParent=False
        curNode=self._head
        if (curNode==None):
            print(Fore.RED+'list is empty, can not create a child'+Style.RESET_ALL)
            return
        else:
            while(curNode!=None):
                if (curNode.data==parent and curNode.child==None):
                    isParent=True
                    curNode.child=Node(child)
                    self._size += 1
                elif (curNode.data==parent and curNode.child!=None):
                    isParent=True
                    tmpNode = self.traverseChild(curNode.child)
                    tmpNode.child = Node(child)
                    self._size += 1
                curNode = curNode.next
            if isParent==False:
                print(colored('{0} does not exist as parent, therefore {1} is not added as child of {0}'
                              .format(str(parent),str(child)),'red'))




    def printList(self):
        curNode=self._head
        while (curNode!=None):
            print(f"\n",Fore.LIGHTYELLOW_EX +str(curNode.data)+Style.RESET_ALL , end=' ')
            if curNode.child!=None:
                tmpNode = curNode.child
                while (tmpNode!=None):
                    print("-> ", Fore.CYAN+(str(tmpNode.data)), end=" ")
                    tmpNode = tmpNode.child
            curNode=curNode.next


mll=multiLevelLinkedList()
mll.createNode(1)
mll.createNode(2)
mll.createNode(3)
mll.createChild(1,2)
mll.createChild(1,3)
mll.createChild(1,4)
mll.createChild(1,8)
mll.createChild(1,9)
mll.createChild(2,4)
mll.createChild(2,5)
mll.createChild(3,6)
mll.createChild(3,7)
mll.createChild(2,10)
mll.createChild(2,11)
mll.createChild(11,12)
mll.createChild(13,14)

mll.printList()

print(Style.RESET_ALL+'\n Size: ',len(mll))