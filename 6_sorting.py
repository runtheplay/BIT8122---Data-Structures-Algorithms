# Time Complexity: Bubble O(n^2), Insertion O(n^2)
def bubble(a):
  a=a[:]
  for i in range(len(a)):
   for j in range(len(a)-1-i):
    if a[j]>a[j+1]: a[j],a[j+1]=a[j+1],a[j]
     print('Pass',i+1,a)
   return a
  
  def insertion(a):
  a=a[:]
  for i in range(1,len(a)):
   k=a[i]; j=i-1
   while j>=0 and a[j]>k: a[j+1]=a[j]; j-=1
    a[j+1]=k
   return a
  arr=[64,34,25,12,22,11,90]
print('Bubble Result',bubble(arr))
print('Insertion Result',insertion(arr))
