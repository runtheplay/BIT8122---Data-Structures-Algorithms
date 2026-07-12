# Time Complexity: Linear O(n), Binary O(log n)
a=list(range(1,40,2)); target=25
lc=0
for i,v in enumerate(a):
  lc+=1
  if v==target: li=i; break
      low,high=0,len(a)-1; bc=0
while low<=high:
  mid=(low+high)//2; bc+=1
  if a[mid]==target: bi=mid; break
      elif a[mid]<target: low=mid+1
      else: high=mid-1
      print('Linear:',li,'comparisons',lc)
print('Binary:',bi,'comparisons',bc)
