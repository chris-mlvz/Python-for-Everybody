
# * File Handle as a Sequence
# xfile = open('mbox.txt')
# for cheese in xfile:
#     print(cheese)

# * Counting Lines in a File
# fhand = open('mbox.txt')
# count = 0
# for line in fhand:
#     count = count + 1
# print('Line Count:', count)

# * Reading the *Whole* File
# fhand = open('mbox.txt')
# inp = fhand.read()
# print(len(inp))
# print(inp[:20])

# * Searching Through a File (fixed)
# fhand = open('mbox.txt')
# for line in fhand:
#     if line.startswith('The'):
#         print(line)

# * Searching Through a File (fixed)
# fhand = open('mbox.txt')
# for line in fhand:
#     line = line.rstrip()
#     if line.startswith('The'):
#         print(line)

# * Skipping with continue
# fhand = open('mbox.txt')
# for line in fhand:
#     line = line.rstrip()
#     if not line.startswith('The'):
#         continue
#     print(line)

# * Prompt for File Name
# fname = input('Enter the file name: ')
# fhand = open(fname)
# count = 0
# for line in fhand:
#     if line.startswith('The'):
#         count = count + 1
# print('There were', count, 'subject lines in', fname)

# * Bad File Names
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()
    
count = 0
for line in fhand:
    if line.startswith('The'):
        count = count + 1
print('There were', count, 'subject lines in', fname)