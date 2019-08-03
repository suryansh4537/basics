class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedlist:
    def __init__(self):
        self.head=None

    def atbeg(self,data):
        newnode=Node(data)
        if self.head==None:
            self.head=newnode
            return

        newnode.next=self.head
        self.head=newnode

    def showall(self):
        nextval=self.head
        while(nextval!=None):
            print(nextval.data)
            nextval=nextval.next

l1=linkedlist()
d=input("enter value at head=")
l1.head=Node(d)
check='y'
while check!='n':
    check=input("enter more nodes(y/n)")
    if check=='y':

        l1.atbeg(input("enter value="))

l1.showall()