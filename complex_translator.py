
    
def translate(phrase):
    translation=""
        
    for letter in phrase:
        if  letter.lower() in"j" :
            
            translation+="x"
        
        elif letter in "aeiouAEIOU":
            
            translation+="g"
        
        elif letter in "wxyzWXYZ":
            
            translation+="5"
        elif letter in "stop":
            
            translation+="/"
        elif letter in "qlñm":
            
            translation+="v"
        else:
            translation+=letter
            
    return translation
while True:
    print(translate(input("Que quieres traducir: ")))
