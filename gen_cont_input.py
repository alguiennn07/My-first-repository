from random import choices,shuffle
import string
def crear(sa):
    while True:
        signos=choices(['@' , '#' , "?" , "¿" '¡' , "!" , '*' , '/' , '-' , '_'],k=2)
        letras=choices(string.ascii_letters+ string.ascii_uppercase,k=4)

        prim_letras=choices(string.ascii_letters + string.ascii_uppercase,k=1)
        numeros=choices(str(i for i in range(0,9)),k=3)

        cuerpo = signos+letras+numeros
        shuffle(cuerpo)
        "".join(cuerpo)

        todo = *prim_letras, *cuerpo
        
        
        
        if "todo" in sa:
            
                cosa3=input("Presiona enter para generar una contraseña con letras, números y símbolos o escribe 'volver' para elegir el tipo.")
                print(*todo, sep="")
                if  "volver" in cosa3:
                    
                    break    
        elif "numeros" in sa:
                cosa=input("Presiona enter para generar una contraseña de sólo números o escribe 'volver' para elegir el tipo.")
            
                numeros2=choices(str(i for i in range(0,9)),k=8)
                print(*numeros2, sep="")
                if  "volver" in cosa:
                    break
        elif "letras" in sa:
                cosa2=input("Presiona enter para generar una contraseña de sólo letras o escribe 'volver' para elegir el tipo.")
            
                letras2=choices(string.ascii_letters+ string.ascii_uppercase,k=8)
                print(*letras2, sep="")
                if  "volver" in cosa2:
                    break
        else:
            print("No disponible")
            break
while True:
    crear(input("Que caracteres quieres que tenga la contraseña?(Todo, letras o numeros)"))
    
