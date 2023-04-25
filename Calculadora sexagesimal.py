aa=["minuto","segundo","hora","dia","semana","mes","año","decada","siglo" , "milenio"]
m,s,h,d,se,me,añ,de,si,mi=aa
m=60 ;s=1;h=3600;d=86400;se=604800;me=2592000;añ=31104000;de=311040000;si=3110400000;mi=3110400000 
a=input("¿Que quieres convertir? ");b=input("¿A qué los quieres pasar? ")
d=(a=="minutos")
if a==True and b=="milisegundos":print("not available")
elif b=="segundos":c=int(input(f"¿Cuántos {a}? "));print(f"{c} {a} equivalen a {c*60} {b}") 
elif b=="dias":c=int(input(f"¿Cuántos {a}? "));print(f"{c} {a} equivalen a {c/1440} {b}") 
elif b=="semanas":c=int(input(f"¿Cuántos {a}? "));print(f"{c} {a} equivalen a {c/10080} {b}") 
elif b=="meses":c=int(input(f"¿Cuántos {a}? "));print(f"{c} {a} equivalen a {c/43800} {b}") 
elif b=="años":c=int(input(f"¿Cuántos {a}? "));print(f"{c} {a} equivalen a {c/525600} {b}") 
elif b=="decadas":c=int(input(f"¿Cuántos {a}? "));print((f"{c} {a} equivalen a {c/5256000} {b}"))
elif b=="siglos":c=int(input(f"¿Cuántos {a}? "));print(f"{c} {a} equivalen a {c/52560000} {b}")
elif b=="milenios":c=int(input(f"¿Cuántos {a}? "));print(f"{c} {a} equivalen a {c/525600000} {b}") 
elif b=="horas":c=int(input(f"¿Cuántos {a}? "));print(f"{c} {a} equivalen a {c/60} hora(s)") 
else:print("que")