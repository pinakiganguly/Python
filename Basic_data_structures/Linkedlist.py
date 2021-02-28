
class node:
    def __init__(self,value):
        self.data=value
        self.next=None




class LL:
    def __init__(self):
        self.head=None
    def add(self,value):
        new_node=node(value)
        new_node.next=self.head
        self.head=new_node
    def add_tail(self,value):
        new_node=node(value)
        if self.head==None:
            self.head=new_node
        else:
            temp=self.head
            while(temp.next!=None):
                temp=temp.next
            temp.next=new_node
    def add_after(self,after,value):
        temp=self.head
        while temp!=None:
            if temp.data==after:
                break
            temp=temp.next
        if temp==None:
            print("Not Found")
        else:
            new_node=node(value)
            new_node.next=temp.next
            temp.next=new_node
    def delete_tail(self):
        temp=self.head
        if(self.head==None):
            print("Empty list")
        else:
            if(temp.next==None):
                self.head=None
                return
            while temp.next.next!=None:
                temp=temp.next
            temp.next=None
    def delete_head(self):
        if self.head==None:
            print("List is empty")
        else:
            self.head=self.head.next
    def delete_val(self,value):
        if self.head.data==value:
            self.delete_head()
            return
        temp=self.head
        if self.head==None:
            print("Empty")
        else:
            while temp.next!=None:
                if temp.next.data==value:
                    break
                temp=temp.next
            if temp.next==None:
                return "Not found"
            else:
                temp.next=temp.next.next
    def search(self,val):
        temp=self.head
        pos=0
        while temp!=None:
            if temp.data==val:
                return pos
            temp=temp.next
            pos+=1
        return "Not Found"
    def replace_max(self,val):
        temp=self.head
        maxi=temp
        while temp!=None:
            if temp.data>maxi.data:
                maxi=temp
            temp=temp.next
        maxi.data=val

    def traverse(self):
        temp=self.head
        while(temp!=None):
            print(temp.data)
            temp=temp.next
    def sum_odd_nodes(self):

        temp = self.head
        counter = 0
        result = 0

        while temp != None:

            if counter %2 != 0:
                result = result + temp.data

            counter+=1
            temp = temp.next

        print(result)
    def reverse(self):
        prev_node=None
        
        current_node=self.head
        while current_node!=None:
            next_node=current_node.next
            current_node.next=prev_node
            prev_node=current_node
            current_node=next_node
        self.head=prev_node
    def change_sent(self):
        temp=self.head
        while temp!=None:
            if temp.data=='*' or temp.data=='/':
                temp.data=" "
                if temp.next.data=='*' or temp.next.data=='/':
                    temp.next.next.data=temp.next.next.data.upper()
                    temp.next=temp.next.next
            temp=temp.next

L=LL()
L.add('T')
L.add('h')
L.add('e')
L.add('*')
L.add('/')
L.add('s')
L.add('k')
L.add('y')
#L.add_tail(9)
#L.add_after(9,14)
#L.delete_tail()
#L.delete_head()
#L.delete_val(8)
#L.replace_max(1)
#print(L.search(9))
L.change_sent()
L.traverse()