

class Node:
    def __init__(self,data):
        self.data=data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head=None

    def lengthfinder(self):
        s=self.head
        length=1
        while s.next!=None:
            s = s.next
            length+=1
        return length


    def append(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
            return

        last=self.head
        while last.next!=None:
            last=last.next
        last.next=new_node

    def printall(self):
        start=self.head
        while start!=None:
            print(start.data)
            start=start.next

    def deletenode(self,key):
        if not key:
            return
        start=self.head
        if start and start.data==key:
            self.head=start.next
            start.next=None
            return
        prev=None
        while start and start.data!=key:
            prev=start
            start=start.next

        prev.next=start.next
        start.next=None

    def deleteDuplicates(self):
        start=self.head
        duplicate=[]
        prev=None
        while start:

            if start.data in duplicate:
                prev.next=start.next
                start=None
            else:
                duplicate.append(start.data)
                prev=start
            start=prev.next

    def fromlast(self,key):
        length=self.lengthfinder()
        start=self.head
        check=True
        while start and check:
            if key>length:
                print("invalid index")
                break
            if key==length:
                print(start.data)

                check=False
            start=start.next
            length-=1



l1=linkedlist()
l1.append("A")
l1.append("B")
l1.append("A")
l1.append("C")
l1.append("C")
l1.append("D")
l1.append("E")
l1.append("F")
#l1.deletenode("A")
l1.deleteDuplicates()
l1.printall()
print()
l1.fromlast(7)


