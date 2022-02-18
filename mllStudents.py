# Student Class
class student:
    def __init__(self):
        self.ID=0
        self.lastName=None
        self.firsttName=None
        self.streetAdd=None
        self.city=None
        self.cityCode=None
        self.zipCode=0

# Node class for Multi Linked List
class StudentMListNode(object) :
    def __init__( self, data ):
        self.data = data
        self.nextById = None
        self.nextByName = None


class multiLevelLinkedList():
    def __init__(self):
        self._listByID=None
        self._size=0

    def addNode(self,std):
        # print(std.ID)
        if self._listByID==None:
            self._listByID = StudentMListNode(std)
            # print(self._listByID.data.ID)
            self._size += 1
        else:
            newNode=StudentMListNode(std)
            curNode = self._listByID
            predNode = curNode
            while curNode!=None:
                predNode = curNode
                curNode= curNode.nextById
            predNode.nextById= newNode
            # print(predNode.nextById.data.ID)
            self._size += 1

    def printlist(self):
        curNode= self._listByID
        while curNode!=None:
            print(curNode.data.ID, curNode.data.lastName)
            curNode = curNode.nextById


# Test Program
import csv

mlll = multiLevelLinkedList()

file = open('student.csv')
type(file)

csvreader = csv.reader(file)

rows = []
for row in csvreader:
    stdobj = student()
    stdobj.ID=row[0]
    stdobj.lastName=row[1]
    stdobj.firstName=row[2]
    stdobj.streetAdd=row[3]
    stdobj.city=row[4]
    stdobj.cityCode=row[5]
    stdobj.zipCode=row[6]
    #rows.append(stdobj)
    # rows.append(row)
    mlll.addNode(stdobj)

for item in rows:
    print('ID: {0}, first Name: {1}'.format(item.ID,item.lastName))

file.close()

mlll.printlist()