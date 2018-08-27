# string is a sequence.
fruit = 'banana'
print('fruit =', fruit, ', fruit[1] =', fruit[1], '\n')

# string indices must be integers.
# fruit[1.5] is invalid.

# len
print('len(fruit) =', len(fruit), '\n')

# traversal
# while
print('while')
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1
print()
# for
print('for')
for letter in fruit:
    print(letter)

# string slice
s = 'Monty Python'
print('s[0:5] =', s[0:5])
print('s[6:12] =', s[6:12])
print('fruit [3:3] =', fruit[3:3], '\n')

# 'str' object does not support item assignment
greeting = 'Hello, world!'
# greeting[0] = 'J'
# new_greeting = 'J' + greeting[1:]

# string method
# upper
word = 'banana'
print('before upper word =', word)
word.upper()
print('after upper word =', word, '\n')
# find
word = 'banana'
print('word =', word)
index = word.find('a')
print('find a index =', index)
index = word.find('na')
print('find na index =', index)
index = word.find('na', 3)
print('find na 3 index =', index)
index = word.find('na', 3, 5)
print('find na 3 5 index =', index, '\n')

# in
print('\'a\' in \'banana\'', 'a' in 'banana')
print('\'seed\' in \'banana\'', 'seed' in 'banana')
