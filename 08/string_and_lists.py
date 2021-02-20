
# * Best Friends: Strings and Lists
# abc = 'With three words'
# stuff = abc.split()
# print(stuff)
# print(len(stuff))
# print(stuff[0])

# print(stuff)
# for w in stuff:
#     print(w)

# * Split
# line = 'A lot                of Spaces'
# etc = line.split()
# print(etc)
# line = 'first;second;third'
# thing = line.split()
# print(thing)
# print(len(thing))
# thing = line.split(";")
# print(thing)
# print(len(thing))

# * More Split
# line = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
# words = line.split()
# print(words)

# * The Double Split Pattern
line = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
words = line.split()
email = words[1]
print(email)
pieces = email.split('@')
print(pieces[1])

