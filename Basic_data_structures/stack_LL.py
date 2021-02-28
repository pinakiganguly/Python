class node:
    def __init__(self,value):
        self.data=value
        self.next=None

class Stack:
    def __init__(self):
        self.top=None
    def isempty(self):
        return self.top==None
    def push(self,value):
        new_node=node(value)
        new_node.next=self.top
        self.top=new_node
    def peek(self):
        if (self.isempty()):
            return "Stack empty"
        else:
            return self.top.data

    def pop(self):
        if(self.isempty()):
            return "Stack empty"
        else:
            self.top=self.top.next
    def traverse(self):
        temp=self.top
        while temp!=None:
            print(temp.data)
            temp=temp.next

S=Stack()
S.push(4)   
S.push(6)
S.push(7)
#print(S.peek())
S.pop()
S.traverse()