class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedlist:
    def __init__(self):
        self.head=None

    def append(self,data):
        newnode=Node(data)
        if self.head==None:
            self.head=newnode
            return
        link=self.head
        while link.next is not None:
            link=link.next
        link.next=newnode

    def showAll(self):
        printnext=self.head
        while printnext!=None:
            print(printnext.data)
            printnext=printnext.next

l1=linkedlist()
d=input("enter data to the head=")
l1.head=Node(d)
check='y'
while check=='y':
    check=input("do you want to enter more?(y/n)")
    if check=='y':
        l1.append(input("enter value at this node="))

l1.showAll()
