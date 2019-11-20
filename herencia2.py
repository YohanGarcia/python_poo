class Pet():
    def __init__(self, breed, name, age):
        self.breed = breed
        self.name = name
        self.age = age
        self.vacs = 0
        self.voice = ''

    def read_vacs(self):
        print(self.name + ' cuneta con ' + str(self.vacs) + ' vacunas.')
        
    def update_vacs(self, number_vacs):
        if number_vacs >= self.vacs:
            self.vacs = number_vacs
        else:
            print("No puedes reducir el numero de vacuans... :@JOLINES!")
            
    def set_voice(self, voice):
        self.voice = voice

class Caraterisca():
    def __init__(self):
        self.ears = ''
        self.tail = ''
        self.fur = ''
        self.body = ''

    def set_caraterisca(self, ears, tail, fur, body):
        self.ears = ears
        self.tail = tail
        self.fur = fur
        self.body = body

    def read_carateristica(self):
        print("orejas: "  + self.ears, 'cola: ' + self.tail, 'pareja: ' + self.fur, "cuerpo: " + self.body, sep="\n")

class Dog(Pet):
    def __init__ (self, breed, name, age):
        super().__init__(breed, name, age)
        self.carateristica = Caraterisca()

    def get_description_dog(self):
        description = self.name + ' Tiene ' + str(self.age) + 'años y es de raza: ' + self.breed
        return description.title()
    
class Fish(Pet):
    def __init__(self, breed, name, age):
         super().__init__(breed, name, age)

    def get_description_dog(self):
        description = self.name + ' Tiene ' + str(self.age) + ' años tiene es de raza ' + self.breed
        return description.title()

    def set_voice(self, voice):
        print("El pez no puede emitir " + voice)



my_dog = Dog("Dalmata", "Kiara", 8)

my_fish = Fish('Payaso', 'nemo', 3)

my_fish.set_voice('Gruñido')

print(my_fish.voice)
    
my_dog.carateristica.set_caraterisca('larga', 'mediana', 'manchado', 'gordinta')
my_dog.carateristica.read_carateristica()