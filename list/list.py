cheeses = ['Cheddar', 'Edam', 'Gouda']
numbers = [42, 123]
empty = []
print(cheeses, numbers, empty, '\n')

print('cheeses[0] =', cheeses[0], '\n')

# the list is variable.
print('before numbers =', numbers)
numbers[1] = 5
print('after numbers =', numbers, '\n')

# is it an element in list?
print('cheeses =', cheeses, '\n')
print('\'Edam\' in cheeses =', 'Edam' in cheeses)
print('\'Brie\' in cheeses =', 'Brie' in cheeses, '\n')

# traversal
for cheese in cheeses:
    print(cheese)
print()
for i in range(len(numbers)):
    print(numbers[i])
print()

# operation
# +
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print('a =', a)
print('b =', b)
print('c =', c, '\n')
# *
d = [0] * 4
print(d, '\n')

# list slice
t = ['a', 'b', 'c', 'd', 'e', 'f']
print(t[1:3])
print(t[:4])
print(t[3:], '\n')

# list method

# append
# append a element
t = ['a', 'b', 'c']
print('before append t =', t)
t.append('d')
print('after append t =', t)
# append a list
t1 = ['a', 'b', 'c']
t2 = ['d', 'e']
print('t1 =', t1)
print('t2 =', t2)
t1.append(t2)
print('t1.append(t2), t1 =', t1, '\n')
# extend
t1 = ['a', 'b', 'c']
t2 = ['d', 'e']
print('t1 =', t1)
print('t2 =', t2)
t1.extend(t2)
print('t1.extend(t2), t1 =', t1, '\n')
# sort
t = ['d', 'c', 'e', 'b', 'a']
print('before sort t =', t)
t.sort()
print('after sort t =', t, '\n')
# sum
t = [1, 2, 3]
print('sum(t) =', sum(t), '\n')

# delete element
# pop
t = ['a', 'b', 'c']
print('before pop t =', t)
x = t.pop(1)
print('after pop t =', t, ', x =', x, '\n')
# del
t = ['a', 'b', 'c']
print('before del t =', t)
del t[1]
print('after del t =', t)
t = ['a', 'b', 'c', 'd', 'e', 'f']
print('before del t =', t)
del t[1:5]
print('after del t =', t, '\n')
# remove
t = ['a', 'b', 'c']
print('before remove t =', t)
t.remove('b')
print('after remove t =', t, '\n')

# convert string to list
# list()
s = 'spam'
print('s =', s)
t = list(s)
print('t =', t, '\n')
# split
s = 'pining for the fjords'
print('before split s =', s)
t = s.split()
print('before split t =', t)
s = 'spam−spam−spam'
print('before split s =', s)
t = s.split('-')
print('before split t =', t, '\n')

# convert list to string
t = ['pining ', 'for', 'the', 'fjords ']
delimiter = '_'
print('before join t =', t)
s = delimiter.join(t)
print('after join s =', s, '\n')

# list and string
# string
a = 'banana'
b = 'banana'
print('string a is b =', a is b)
# list
a = [1, 2, 3]
b = [1, 2, 3]
print('list a is b =', a is b)
# list reference
a = [1, 2, 3]
b = a
print('list reference a is b =', a is b)
