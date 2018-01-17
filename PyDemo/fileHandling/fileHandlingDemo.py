import os
from pathlib import Path

path = '/home/amol/temp/test'
print(os.path.exists(path))

# file1 = open(path+'/test.txt', 'r')
# file2 = open('test1.txt', 'w')
# for line in file1:
#     file2.write(line.replace('jumps', 'bumps'))

loc = Path(path)
for p in loc.iterdir():
        print(p)
        if p.is_file():
            print("true")
            if str(p).__contains__(".txt"):
                print(open(str(p), 'r').read())
