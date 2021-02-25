
# * Using re.search() like find()
# import re
# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
#     if line.find('From:') >= 0:
#         print(line)

# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
#     if re.search('From:', line):
#         print(line)

# * Using re.search() like startswith()
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.match('From:', line):
        print(line)
