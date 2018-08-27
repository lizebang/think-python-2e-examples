import os
import dbm
import pickle

fout = open('output.txt', 'w')
line1 = "This here's the wattle.\n"
fout.write(line1)
fout.close()

fout = open('output.txt', 'w')
x = 52
fout.write(str(x))  # overwrite

# format operator
camels = 42
print('%d' % camels)
print('In %d years I have spotted %g %s.' % (3, 0.1, 'camels '), '\n')

# function
print(os.getcwd())
print(os.path.abspath('output.txt'))
print(os.path.exists('output.txt'))
print(os.path.isdir('output.txt'))
print(os.listdir(os.getcwd()), '\n')

# catch exception
try:
    fin = open('bad_file')
except OSError:
    print('Something went wrong.')
print()

# database
try:
    db = dbm.open('captions', 'c')
    db['cleese.png'] = 'Photo of John Cleese.'
    print(db['cleese.png'])
    db['a'] = 'a'
    db['b'] = 'b'
    db['c'] = 'c'
finally:
    db.close()

# pickle
t1 = [1, 2, 3]
s = pickle.dumps(t1)
t2 = pickle.loads(s)
print('t1 =', t1)
print('s =', s)
print('t2 =', t2, '\n')

# pipe
cmd = 'ls -l'
fp = os.popen(cmd)
res = fp._stream.read()
print('res =', res)
stat = fp.close()
print('stat =', stat, '\n')
