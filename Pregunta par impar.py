numero=int(input("ingrese su número, le diremos si es par o impar "))
print(numero) 
if numero % 2 == 0:
    print("Ese número es par, a mí no me engañas")
else:
    print("Ese número es impar, crack.")
   
b=(input("¿Quieres añadir otro? "))
if b == "si":c=int(input("Dime otro número y te diré si es par o impar otra vez"))
if b == "no":print("No te cagues")
if c % 2 == 0:
    print("paaaaar")
else:print("impaar")