t = 'a', 'b', 'c', 'd', 'e'
t = ('a', 'b', 'c', 'd', 'e')

# tuple
t1 = 'a',
print('t1 type', type(t1))

# str
t2 = ('a')
print('t2 type', type(t2))

# tuple
t3 = tuple()
print('t3 type', type(t3), '\n')

# convert strong to tuple
t = tuple('lupins')
print('t =', t, '\n')

# operation
t = ('a', 'b', 'c', 'd', 'e')
print('t[0] =', t[0])
print('t[3:5] =', t[3:5])
# t[0] = 'A'        object doesn 't support item assignment
t = ('A',) + t[1:]
print('t =', t)
print('(0, 1, 2000000) < (0, 3, 4)', (0, 1, 2000000) < (0, 3, 4), '\n')

# swap
a = 1
b = 2
print('before a =', a, ', b =', b)
a, b = b, a
print('after a =', a, ', b =', b, '\n')


def min_max(t):
    return min(t), max(t)


def printall(*args):
    print(args)


# zip
s = 'abc'
t = [0, 1, 2]
for pair in zip(s, t):
    print(pair)
print()

print(list(zip(s, t)), '\n')

t = [('a', 0), ('b', 1), ('c', 2)]
for letter, number in t:
    print(number, letter)
print()

for index, element in enumerate('abc'):
    print(index, element)
print()

# dict
d = {'a': 0, 'b': 1, 'c': 2}
t = d.items()
print('d =', d)
print('t =', t, '\n')

d = dict(zip('abc', range(3)))
print('d =', d, '\n')

d = {("last", "first"): "number"}
print('d =', d)
