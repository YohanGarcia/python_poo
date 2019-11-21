class Telefono:
    def __init__(self):
        pass

    def llamar(self):
        print('llamando...')
    
    def ocupado(self):
        print('ocupado...')

class Camara:
    def __init__(self):
        pass

    def fotografia(self):
        print('tomando fotos...')

class  Reproducion:
    def __init__(self):
        pass

    def reproduciendomusica(self):
        print('reproduciendo musica')
    
    def reproducirvideo(self):
        print('reproducir un video')

class smartphone(Telefono,Camara,Reproducion):
    def __init__(self):
        print('telefono apagado')

movil = smartphone()
print(dir(movil))