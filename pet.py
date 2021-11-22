class Pet:
    'Class for all pets'
    petCount = 0

    def __init__(self, name, kind):
        self.isfed = False
        self.name = name
        self.kind = kind
        Pet.petCount += 1

    def displayPet(self):
        print ('Name: ', self.name, ', Kind: ', self.kind, ', Fed: ', self.isfed)
