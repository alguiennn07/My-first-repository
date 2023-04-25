def saludo_al_salir(nombre):
    mensaje=("Hola "+ nombre)
    return mensaje
print(saludo_al_salir("Carlos"))

def circle_area(rad):
    area=(3.14*(rad*rad))
    return area
print(circle_area(5))

def square_area(side):
    area=side*side
    return area
print(square_area(25))

#PARA CALCULAR EL ÁREA CON UN INPUT:
def area_cuad(lado):
    area=lado*lado
    return area
a=int(input("lado: "))
print(area_cuad(a))





