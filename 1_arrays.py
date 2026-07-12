# Time Complexity: Read O(1), Update O(1), Traverse O(n), Max O(n), Insert O(n)
marks = [75, 82, 90, 68, 88]

print('Original Array:', marks)

index = 2
print('Read at index 2:', marks[index])

marks[1] = 85
print('After update index 1:', marks)

print('Traverse:')
for m in marks:
    print(m, end=' ')
print()

print('Maximum value:', max(marks))

insert_index = 3
new_value = 95
print('Before insertion:', marks)
marks.append(None)
for i in range(len(marks)-1, insert_index, -1):
    marks[i] = marks[i-1]
marks[insert_index] = new_value
print('After insertion:', marks)
