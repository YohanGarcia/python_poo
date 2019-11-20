
saldo = 100
fruta = ["pera","manzana","uva"]

print("esto es lo que hay de frutas")
fruta.insert(3, "mango")
print(fruta)


fruta = input("ingrese fruta:")
pera = 50
manzana = 25
uva = 25


while fruta != "exit":
    if fruta ==fruta[0] and fruta!=fruta[1] and fruta!=fruta[2]:
        print("no tenemos")
    else:
        fruta = pera
        fruta = manzana
        fruta = uva
        uva = 25
        pera = 50
        manzana = 25
        saldo -= fruta
    fruta = input(f"saldo{saldo}\ningrese el nombre de la frutas:")
    if saldo <=0:
        fruta = input(f"ya no tiene saldo{saldo} suficiente\npara salir escribe 'exit' gg:")
print("adios")

    