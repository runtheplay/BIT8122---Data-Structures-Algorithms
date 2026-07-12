# Time Complexity: Push/Pop/Peek O(1), Bracket Check O(n)
class Stack:
def __init__(self): self.a=[]
def push(self,x): self.a.append(x)
def pop(self): return self.a.pop() if self.a else None
def peek(self): return self.a[-1] if self.a else None
def empty(self): return len(self.a)==0

def balanced(s):
st=Stack(); p={')':'(',']':'[','}':'{'}
for c in s:
if c in '([{': st.push(c)
elif c in p:
if st.empty() or st.pop()!=p[c]: return False
return st.empty()
print('Balanced:', balanced('{[()()]}'))
