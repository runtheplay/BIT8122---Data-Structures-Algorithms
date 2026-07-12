# Time Complexity: Read O(1), Update O(1), Traverse O(n), MaxO(n), Insert O(n)
marks=[75,82,90,68,88]
print('Original:',marks)
print('Read index 2:',marks[2])
marks[1]=85
print('After update:',marks)
print('Traverse:',end=' ')
for x in marks: print(x,end=' ')
    print() 
mx=marks[0]
for x in marks:
    if x>mx: mx=x
        print('Max:',mx)
arr=marks[:]
print('Before insertion:',arr)
idx,val=3,95
arr.append(None)
for i in range(len(arr)-1,idx,-1):
    arr[i]=arr[i-1]
    arr[idx]=val
print('After insertion:',arr)
