#generador de contraseñas

import string

from random import choices,shuffle,choice


def crear():
    while True:
        opcion = input("¿Qué tipo de contraseña quieres generar? (letras, numeros o todo): ")
        
        if opcion == "todo":
            signos = choices(['@', '#', '?', '¿', '¡', '!', '*', '/', '-', '_'], k=2)
            letras = choices(string.ascii_letters + string.ascii_uppercase, k=4)
            prim_letras = choices(string.ascii_letters + string.ascii_uppercase, k=1)
            numeros = choices([str(i) for i in range(0, 9)], k=3)

            cuerpo = signos + letras + numeros
            shuffle(cuerpo)
            todo = [*prim_letras, *cuerpo]
            print("Contraseña generada: " + "".join(todo))
            
        elif opcion == "numeros":
            numeros2 = choices([str(i) for i in range(0, 9)], k=8)
            print("Contraseña generada: " + "".join(numeros2))
            
        elif opcion == "letras":
            letras2 = choices(string.ascii_letters + string.ascii_uppercase, k=8)
            print("Contraseña generada: " + "".join(letras2))
            
        elif opcion == "salir":
            break
            
        else:
            print("Opción inválida. Por favor, elige entre letras, numeros o todo.")
            continue
            
        
        
        
        
    
        
    

crear()
    
    
    
   

    



