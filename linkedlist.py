
class Node:

    def __init__(self,data):
        self.data=data
        self.next=None

class linkedlist:
    def __init__(self):
        self.head=None

    def printall(self):
        printnext=self.head
        while printnext!=None:
            print(printnext.data)
            printnext=printnext.next

    def append(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
            return

        last=self.head
        while last.next!=None:
            last=last.next

        last.next=new_node

    def swap(self,key1,key2):
        if key1==key2:
            return

        prev_1=None
        current1=self.head
        while current1 and current1.data!=key1:
            prev_1=current1
            current1=current1.next

        prev_2=None
        current2=self.head
        while current2 and current2.data!=key2:
            prev_2=current2
            current2=current2.next

        if prev_1:
            prev_1.next=current2
        else:
            self.head=current2
        if prev_2:
            prev_2.next=current1
        else:
            self.head=current1

        current1.next,current2.next=current2.next,current1.next

    def reverse(self):
        prev=None
        current=self.head
        while current:
            nxt=current.next
            current.next=prev
            prev=current
            current=nxt
        self.head=prev


    def deletenode(self):
        pass


list1=linkedlist()
list1.append("a")
list1.append("b")
list1.append("c")
list1.append("d")
list1.swap("d","a")
#list1.swap("d","c")
#list1.printall()
#list1.reverse()
list1.printall()