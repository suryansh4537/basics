class Node:
    def __init__(self,data):
        self.data=data
        self.nextval=None
        self.prev=None

class doublylinkedlist:
    def __init__(self):
        self.head=None

    def append(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            return

        currentnode=self.head
        while currentnode.nextval:
