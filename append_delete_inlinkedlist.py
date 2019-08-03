class Node:
    def __init__(self,data):
        self.data=data
        self.nextval=None

class linkedlist:
    def __init__(self):
        self.head=None

    def append(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
            return
        last=self.head
        while last.nextval!=None:
            last=last.nextval
        last.nextval=new_node

    def showall(self):
        start=self.head
        while start!=None:
            print(start.data)
            start=start.nextval

    def deletenode(self,key):
        point=self.head
        if point and point.data==key:
            self.head=point.nextval
            point.nextval=None
            return

        prev = None
        while point and point.data!=key:
            prev = point
            point=point.nextval

        prev.nextval=point.nextval
        point.nextval=None

    def deletewithindex(self,pos):
        index=0
        currentnode=self.head
        if currentnode and pos==index:
            self.head=currentnode.nextval
            currentnode.nextval=None
            return
        prev=None
        while index!=pos and currentnode.nextval!=None:
            index+=1
            prev=currentnode
            currentnode=currentnode.nextval

        if currentnode.nextval==None:
            print("not in the list")

        prev.nextval=currentnode.nextval
        currentnode.nextval=None



l1=linkedlist()
l1.append("a")
l1.append("b")
l1.append("c")
l1.append("d")
#l1.deletenode("a")
l1.deletewithindex(4)
l1.showall()