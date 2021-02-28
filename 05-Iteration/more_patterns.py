
# * Counting in a Loop
# zork = 0
# print('Before', zork)
# for thing in [9, 41, 12, 3, 74, 15]:
#     zork = zork + 1
#     print(zork, thing)
# print('After', zork)

# * Summing in a Loop
# zork = 0
# print('Before', zork)
# for thing in [9, 41, 12, 3, 74, 15]:
#     zork = zork + thing
#     print(zork, thing)
# print('After', zork)

# * Finding the Average in a Loop
# count = 0
# sum_total = 0
# print('Before', count, sum_total)
# for value in [9, 41, 12, 3, 74, 15]:
#     count = count + 1
#     sum_total = sum_total + value
#     print(count, sum_total,  value)
# print('After', count, sum_total,  sum_total / count)

# * Filtering in a Loop
# print('Before')
# for value in [9, 41, 12, 3, 74, 15]:
#     if value > 20:
#         print('Large number', value)
# print('After')

# * Search Using a Boolean Variable
# found = False
# print('Before', found)
# for value in [9, 41, 12, 3, 74, 15]:
#     if value == 3:
#         found = True
#     print(found, value)
# print('After', found)

# * How to find the smallest value
smallest = None
print('Before', smallest)
for value in [9, 41, 12, 3, 74, 15]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)
print('After', smallest)
