
# * Slicing Strings
# s = 'Mothy Python'
# print(s[0:4])
# print(s[6:7])
# print(s[6:20])

# * String Concatenation
# a = 'Hello'
# b = a + 'There'
# print(b)
# c = a + ' ' + 'There'
# print(c)

# * Using in as a logical Operator
# fruit = 'banana'
# print('n' in fruit)
# print('m' in fruit)
# print('nan' in fruit)
# if 'a' in fruit:
#     print('Found it!')

# * String Comparison
# word = 'strawberry'
# if word == 'banana':
#     print('All right, bananas')
# if word < 'banana':
#     print('Your word,' + word + ', comes before banana.')
# elif word > 'banana':
#     print('Your word,' + word + ', comes after banana.')
# else:
#     print('All right, bananas')

# * String Library
# greet = 'Hello Bob'
# zap = greet.lower()
# print(zap)
# print(greet)
# print('Hi There'.lower())

# stuff = 'Hello word'
# print(type(stuff))
# print(dir(stuff))

# * Searching a String
# fruit = 'bananas'
# pos = fruit.find('na')
# print(pos)
# aa = fruit.find('z')
# print(aa)

# * Making everything UPPER CASE
# greet = 'Hello Bob'
# nnn = greet.upper()
# print(nnn)
# www = greet.lower()
# print(www)

# * Search and Replace
# greet = 'Hello Bob'
# nstr = greet.replace('Bob', 'Jane')
# print(nstr)
# nstr = greet.replace('o', 'x')
# print(nstr)

# * Stripping Whitespace
# greet = '   Hello Bob   '
# print(greet.lstrip())
# print(greet.rstrip())
# print(greet.strip())

# * Prefixes
# line = 'Please have a nice day'
# print(line.startswith('Please'))
# print(line.startswith('p'))

# * Parsing and Extracting
# data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
# atpos = data.find('@')
# print(atpos)
# sppos = data.find(' ',atpos)
# print(sppos)
# host = data[atpos+1: sppos]
# print(host)

# * Two Kinds of Strings
x = '사랑'
print(type(x))
x = u'사랑'
print(type(x))
