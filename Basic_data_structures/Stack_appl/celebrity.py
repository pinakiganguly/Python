L=[ 
    [0,0,1,1],
    [0,0,1,0],
    [0,0,0,0],
    [0,0,1,0]
]
class Node:

  def __init__(self,value):
    self.data = value
    self.next = None

class Stack:

  def __init__(self):
    self.top = None

  def push(self, value):

    new_node = Node(value)

    new_node.next = self.top

    self.top = new_node

  def pop(self):

    if self.top is None:
      return "Stack Empty"
    else:
      data = self.top.data
      self.top = self.top.next
      return data

  def is_empty(self):
    return self.top == None

  def peek(self):

    if self.top is None:
      return "Stack Empty"
    else:
      return self.top.data

  def traverse(self):

    temp = self.top

    while temp is not None:
      print(temp.data,end=' ')
      temp = temp.next

  def size(self):

    temp = self.top
    counter = 0

    while temp is not None:
      counter+=1
      temp = temp.next

    return counter

def find_the_celeb(L):

  s = Stack()

  for i in range(len(L)):
    s.push(i)

  while s.size() >= 2:

    i = s.pop()
    j = s.pop()

    if L[i][j] == 0:
      # j is not a celebrity
      s.push(i)
    else:
      # i is not a celeb
      s.push(j)

  celeb = s.pop()

  for i in range(len(L)):

    if i != celeb:
      if L[i][celeb] == 0 or L[celeb][i] == 1:
        print("No one is a celebrity")
        return

  print("The celebrity is",celeb)
find_the_celeb(L)