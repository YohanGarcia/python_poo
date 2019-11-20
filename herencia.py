class Pet():
    def __init__(self, bread, name, age):
        self.bread = bread
        self.name = name
        self.age = age
        self.vacs = 0

    def get_description_dog(self):
        descripiton = self.name + ' Tiene ' +str(self.age) + ' años y es de raza:  ' + self.bread
        return descripiton.title()

    def read_vacs(self):
        print(self.name  + ' cuenta con ' + str(self.vacs) + ' vacunas. ')

    def updatte_vacs(self, number_vacs):
        
        if number_vacs >= self.vacs:
            if self.bread == "Dalmata":
                print("No se puede vacanar")
                return 
            self.vacs = number_vacs

        else:
            print("No puede reducir el nimero de vacunas... :@JOLINES!")
            
class Dog(Pet):
    def __init__(self, breed, name, age):
        super().__init__(breed, name, age)

    def get_description_dog(self):
        descripiton = self.name + ' Tiene ' +str(self.age) + ' años y es de raza:  ' + self.bread
        return descripiton.title()       
         
my_dog = Dog("Dalmata", 'Kiara', 8)

my_dog.updatte_vacs(10)

print(my_dog.read_vacs()) 

print(my_dog.get_description_dog())