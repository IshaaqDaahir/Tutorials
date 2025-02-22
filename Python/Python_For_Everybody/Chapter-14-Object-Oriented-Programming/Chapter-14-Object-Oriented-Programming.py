# stuff = list()
# stuff.append('python')
# stuff.append('chuck')
# stuff.sort()
# print(stuff[0])
# print(stuff.__getitem__(0))
# print(list.__getitem__(stuff, 0))
# print(dir(stuff))

# ElevatorCconversion Program
""" usf = input('Enter the US Floor Number: ')
wf = int(usf) - 1
print('Non-US Floor Number is', wf) """

""" class PartyAnimal:
    x = 0
    
    def __init__(self):
        print("I am constructed")
    
    def party(self):
        # self.x += 1
        self.x = self.x + 1
        print('So far', self.x)
        
    def __del__(self):
        print("I am destructed", self.x)
        
an = PartyAnimal()
an.party()
an.party()
# PartyAnimal.party(an)
an = 42
print("an contains", an)

# print('Type', type(an))
# print("Dir", dir(an))
# print("Type", type(an.x))
# print("Type", type(an.party)) """

# When we construct multiple objects from our class, we might want to set up different initial values for each of the 
# objects. We can pass data to the constructors to give each object a different initial value:
class PartyAnimal:
    x = 0
    name = ""
    def __init__(self, nam):
        self.name = nam    
        print(self.name, "constructed")
        
    def party(self):
        self.x = self.x + 1
        print(self.name, "party count", self.x)

s = PartyAnimal('Sally')
j = PartyAnimal('Jim')

s.party()       
j.party()
s.party()

# from party import PartyAnimal

# class CricketFan(PartyAnimal):
#     points = 0
#     def six(self):
#         self.points += + 6
#         self.party()
#         print(self.name, "points", self.points)
        
# s = PartyAnimal("Sally")
# s.party()
# j = CricketFan("Jim")
# j.party()
# j.six()  
# print(dir(j))





