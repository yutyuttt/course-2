class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

import pickle, pathlib # pickle for storage, hehe
file_path = pathlib.Path('data') / 'points.ser' # file on drive
points_written = [Point(x, x**2) for x in range(20)] # some data
print(points_written[-1]) # last point written

# serialize / pickle onto drive
f = open(file_path, 'wb') # open file for writing binary data
pickle.dump(points_written, f) # save data into file
f.close() # close file

# deserialize / unpickle from drive
f = open(file_path, 'rb') # open for reading binary data
points_read = pickle.load(f) # read and return data
f.close() # close file
print(points_read[-1]) # last point read

import pathlib

# under directory data, file data.ser
file_path = pathlib.Path('data') / 'data.ser'
if file_path.exists():
    print('reading', file_path)
else:
    print('no file', file_path)

import pathlib
file_path = pathlib.Path('data') / 'points.txt'
points_written = [Point(x, x**2) for x in range(20)] # some data
# write data onto drive: x y on each line
f = open(file_path, 'w') # open file for writing (text) data
for p in points_written: print(p.x, p.y, file=f) # print data
f.close() # close file

# read data from file
f = open(file_path) # open file (for reading text)
points_read = []
for line in f: # iterate over lines
    [x, y] = [int(word) for word in line.split()] # extract x, y
    points_read.append(Point(x, y))
f.close() # close file
print(points_written[-1], points_read[-1]) # check against orig

import pathlib
f = open(pathlib.Path('data') / 'points.txt')
for line in f:
    print(line)
f.close()

import pathlib
file_path = pathlib.Path('data') / 'points.txt'
with open(file_path) as f: # with establishes new context
    for line in f:
        print(line, end='')
# context closes, file closed automatically

try:
    import pathlib
    file_path = pathlib.Path('data') / 'points.txt'
    with open(file_path) as f:
        points_read = []
        for line in f: # traverse lines
            # extract x, y
            [x, y] = [int(word) for word in line.split()]
            points_read.append(Point(x, y))
    print(points_read[-1])
except Exception as e: # handle any exception raised
    print('exception:', e)
