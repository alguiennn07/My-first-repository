def solution(inputString):
    inputString=inputString.lower().replace(" ", " ")
    
    if inputString==inputString[::-1]:
        return True
    else:return False
inputString=input("PALABRA: ")
if solution(inputString):
    print("Palíndromo")
else: print("No palíndromo" )
