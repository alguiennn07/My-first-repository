nomina=int(input("¿Cuánto ganas?"))
gastos=int(input("¿Cuánto gastas al mes?"))
beneficios=nomina-gastos


if (beneficios <0):print("Es imposible que gastes más de lo que ganas")
if False:print("Tus beneficios mensuales son de" , beneficios  , "€")
if beneficios>150:print("Ganas mucho");print("Gastas el",round(gastos/nomina*100), "% de lo que ganas")
elif beneficios>100:print("Ganas lo promedio");print("Gastas el",round(gastos/nomina*100), "% de lo que ganas")
elif beneficios>0:print("ganas muy poco");print("Gastas el",round(gastos/nomina*100), "% de lo que ganas")
