# Time Complexity: Head Insert O(1), Tail Insert O(n), Delete O(n), Traverse O(n)
class Node:
def __init__(self,d): self.data=d; self.next=None
class LinkedList:
def __init__(self): self.head=None
def insert_head(self,d): n=Node(d); n.next=self.head; self.head=n
def insert_tail(self,d):
n=Node(d)
if not self.head: self.head=n; return
c=self.head
while c.next: c=c.next
c.next=n
def delete(self,v):
c=self.head; p=None
while c:
if c.data==v:
if p: p.next=c.next
else: self.head=c.next
return
p,c=c,c.next
def traverse(self):
c=self.head
while c: print(c.data,end=' -> '); c=c.next
print('None')
ll=LinkedList(); ll.insert_head(20); ll.insert_head(10); ll.insert_tail(30); ll.insert_tail(40); ll.traverse(); ll.delete(30); ll.traverse()
