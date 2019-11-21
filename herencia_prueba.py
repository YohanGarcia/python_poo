class Calculadora:
    def __init__(self,numero):
        self.n = numero
        self,datos = [int(input('ingrese datos '+str(i+1)+ ' = '))for q in range(self.n)]

class op_basicas(Calculadora):
    def __init__(self):
        Calculadora.__init__(self,2)
    
    def suma(self):
        a,b = self.datos
        s = a + b
        print('el resultado es ',s)

    def resta(self):
        a,b = self.datos
        r = a - b
        print('el resutado es n',r)

class raiz(Calculadora):
    def __init__(self):
        Calculadora.__init__(self,1)

    def __init__(self):
        import math
        a, = self.datos
        print('el resultado es ',math.sqrt(a))