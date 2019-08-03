class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedlist:
    def __init__(self):
        self.head=None

    def inbetween(self,element,d):
        if element==None:
            print("element not present")
            return
        newnode=Node(d)
        newnode.next=element.next
        element.next=newnode

    def showall(self):
        link=self.head
        while link!=None:
            print(link.data)
            link=link.next

l1=linkedlist()
l1.head=Node("moday")
l2=Node("tuesday")
l3=Node("wednesday")
l4=Node("thursday")
l1.head.next=l2
l2.next=l3
l3.next=l4

l1.inbetween(l1.head,"friday")

l1.showall()