class Queue:
    def __init__(self,size):
        self.size=size
        self.queue=[None]*self.size
        self.front=-1
        self.rear=-1

    def enqueue(self,value):
        if self.rear==self.size-1:
            return "Queue is full"
        else:
            self.rear+=1
            self.queue[self.rear]=value
    def dequeue(self):
        if self.rear==self.front:
            return "Queue is empty"
        else:
            self.front+=1
            if self.rear==self.front:
                self.front=-1
                self.rear=-1
    def traverse(self):
        for i in range(self.front+1,self.rear+1):
            print(self.queue[i],end=' ')
    def front_item(self):
        if self.front==self.rear:
            return "Queue is empty"
        else:
            return self.queue[self.front+1]
    def rear_item(self):
        if self.front==self.rear:
            return "queue is empty"
        else:
            return self.queue[self.rear]

def fun(num):
    if(num==0):
        return 0
    else:
        queue.enqueue(num%10)
        res=fun(num//10)
        res=res*10+queue.dequeue()
        return res
queue = Queue(100)
print(fun(123))
