
# * Multiway
x = 0
x = 5
x = 20
# if x < 2:
#     print('small')
# elif x < 10:
#     print('Medium')
# else:
#     print('LARGE')
# print('All done')

# if x < 2:
#     print('small')
# elif x < 10:
#     print('Medium')
# elif x < 20:
#     print('Big')
# elif x < 40:
#     print('Large')
# elif x < 100:
#     print('Huge')
# else:
#     print('Ginormous')

# * Multi-way Puzzles
# x = 2
# if x < 2:
#     print('Below 2')
# elif x >= 2:
#     print('Two or more')
# else:
#     print('Something else')

# x = 5
# if x < 2:
#     print('Below 2')
# elif x < 20:
#     print('Below 20')
# elif x < 10:
#     print('Below 10')
# else:
#     print('Something else')

# * Try except
# astr = 'Hello Bob'
# try:
#     istr = int(astr)
# except:
#     istr = -1

# print('First', istr)

# astr = '123'
# try:
#     istr = int(astr)
# except:
#     istr = -1

# print('Second', istr)

# * Try/Except
# astr = 'Bob'
# try:
#     print('Hello')
#     istr = int(astr)
#     print('There')
# except:
#     istr = -1
# print('Done', istr)

# * Sample try/except
rawdtr = input('Enter a number:')
try:
    ival = int(rawdtr)
except:
    ival = -1

if ival > 0:
    print('Nice work')
else:
    print('Not a number')