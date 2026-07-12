# Time Complexity: Insert O(n), BFS O(n), DFS O(n)
from collections import deque
class Node:
  def __init__(self,d): self.data=d; self.left=None; self.right=None
    class Tree:
      def __init__(self): self.root=None
        def insert(self,d):
          n=Node(d)
          if not self.root: self.root=n; return
            q=deque([self.root])
while q:
  t=q.popleft()
if not t.left: t.left=n; return
  if not t.right: t.right=n; return
    q.extend([t.left,t.right])
def bfs(self):
  q=deque([self.root])
while q:
  t=q.popleft(); print(t.data,end=' ')
if t.left:q.append(t.left)
  if t.right:q.append(t.right)
    print()
def dfs(self,node):
  if node: print(node.data,end=' '); self.dfs(node.left); self.dfs(node.right)
    tr=Tree()
for i in range(1,8): tr.insert(i)
  print('BFS:'); tr.bfs(); print('DFS:'); tr.dfs(tr.root); print()
