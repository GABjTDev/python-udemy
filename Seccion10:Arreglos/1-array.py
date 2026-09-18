from array import array

a = array( 'i', [1, 2, 3, 4, 5] )
print(a[0])
print(a[-1])
a.append(6)
print(a)

for value in a:
    print(value, end=' ')


s = array('w', ['a', 'b', 'c'])
print(s)