# must create a dict first
eng2sp = dict()
eng2sp['one'] = 'uno'
print('eng2sp =', eng2sp, '\n')

eng2sp = {'one': 'uno', 'two': 'dos', 'three ': 'tres'}
print('eng2sp =', eng2sp)
# if not exist, an exception is thrown.
print('eng2sp[\'two\'] =', eng2sp['two'], '\n')

# len
print('len(eng2sp) =', len(eng2sp), '\n')

# is it a key in the dict?
print('\'one\' in eng2sp =', 'one' in eng2sp)
print('\'uno\' in eng2sp =', 'uno' in eng2sp, '\n')

# is it a value in the dict?
vals = eng2sp.values()
print('\'uno\' in vals =', 'uno' in vals)


def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


h = histogram('brontosaurus')
print(histogram(h), '\n')

# traversal
h = histogram('parrot')
# unordered
print('unordered')
for c in h:
    print(c, '---', h[c])
print()
# ordered
print('ordered')
for c in sorted(h):
    print(c, '---', h[c])


def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise LookupError()     # raise -- trigger exception
