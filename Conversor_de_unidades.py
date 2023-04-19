#convertir millas a km
unidades=["millas","libras"]
primera,segunda=unidades
unidad=input("¿Qué unidad quieres conversar?¿Libras o Millas? ")
km=1.60934
kilogramos=0.453592

if unidad==primera:
        print(f"De acuerdo, has elegido {unidad}")
        millas=aaa=(int(input("Millas: ")))
        print(f"{millas} millas equivalen a {millas *km} kilómetros")
        aa=input(f"¿Quieres conversar {segunda}? ")
        if aa == "si":aaa=int(input("libras: "))
        print(f"{aaa} libras equivalen a {aaa*0.453592} ")
        if aa == "no":print("Vale, gracias por usar esta app")
       

if unidad==segunda:
    print(f"De acuerdo, has elegido {unidad}")
    libras=(int(input("Libras: ")))
    print(f"{libras} libras equivalen a {libras * kilogramos} kilogramos")
    bb=input(f"¿Quieres conversar {primera}? ")
    if bb=="si":bbb=int(input("millas: "))
    print(f"{bbb} millas equivalen aa {millas*1.60934}")
    if bb == "no":print("Vale, gracias por usar esta app")


elif type(unidad)== str:print("NO disponible")
