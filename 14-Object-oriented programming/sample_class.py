
# * EXample class
class PartyAnimal:
    x = 0

    def party(self):
        self.x = self.x + 1
        print("So far", self.x)


an = PartyAnimal()

an.party()
an.party()
an.party()

print("Type", type(an))
print("DIr", dir(an))

# * A Nerdy Way to FInd Capabilities
# x = list()
# print(type(x))
# print(dir(x))

# * Try dir() with a String
# y = 'Hello there'
# print(dir(y))
