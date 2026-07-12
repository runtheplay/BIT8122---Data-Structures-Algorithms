# Time Complexity: Enqueue O(1), Dequeue O(1), Peek O(1)
class Queue:
def __init__(self,cap=20):
self.a=[None]*cap; self.front=0; self.rear=0; self.size=0
def enqueue(self,x):
self.a[self.rear]=x; self.rear=(self.rear+1)%len(self.a); self.size+=1
def dequeue(self):
if self.size==0:return None
x=self.a[self.front]; self.front=(self.front+1)%len(self.a); self.size-=1; return x
def peek(self): return None if self.size==0 else self.a[self.front]
def state(self): return [self.a[(self.front+i)%len(self.a)] for i in range(self.size)]
q=Queue(); q.enqueue(10); print(q.state()); q.enqueue(20); print(q.state()); q.enqueue(30); print(q.state()); print('Peek',q.peek()); q.dequeue(); print(q.state())
