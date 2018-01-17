import os

path = '/home/amol/temp/test'
print(os.path.exists(path))

file1 = open(path+'/test.txt', 'r')
file2 = open('test1.txt', 'w')
for line in file1:
    file2.write(line.replace('jumps', 'bumps'))