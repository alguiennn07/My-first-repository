#NO TERMINADO


#Conversor de divisas
dolar=1
euro=1.11
gbp=1.54
pes=0.056
antigua=input("¿Qué quieres conversar? ")
nueva=input("¿A qué los quires pasar? ")
cuanto=int(input(f"¿Cuántos  {antigua}?"))
#Convertir dolar
if antigua=="dolar" and nueva =="pesos":print(f"{cuanto} {antigua} equivalen a {dolar/pes*cuanto} {nueva}")
if antigua=="dolar" and nueva =="euros":print(f"{cuanto} {antigua} equivalen a {dolar/euro*cuanto} {nueva}")
if antigua=="dolar" and nueva =="libras":print(f"{cuanto} {antigua} equivalen a {dolar/gbp*cuanto} {nueva}")
#Convertir euro
if antigua=="euro" and nueva =="pesos":print(f"{cuanto} {antigua} equivalen a {euro/pes*cuanto} {nueva}")
if antigua=="euro" and nueva =="euros":print(f"{cuanto} {antigua} equivalen a {euro/dolar*cuanto} {nueva}")
if antigua=="euro" and nueva =="libras":print(f"{cuanto} {antigua} equivalen a {euro/gbp*cuanto} {nueva}")
#Convertir libra
if antigua=="libras" and nueva =="pesos":print(f"{cuanto} {antigua} equivalen a {gbp/pes*cuanto} {nueva}")
if antigua=="libras" and nueva =="euros":print(f"{cuanto} {antigua} equivalen a {gbp/euro*cuanto} {nueva}")
if antigua=="libras" and nueva =="dolar":print(f"{cuanto} {antigua} equivalen a {gbp/dolar*cuanto} {nueva}")






