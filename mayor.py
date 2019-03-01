positivos=0
cero=0
negativos=0


for x in range(0,10):
    x=int(input("ingrese un numero "))
    if x==0:
            cero=cero + 1
            
    else:
        if x>0:
            positivos= positivos + 1
           
        else:
            negativos= negativos + 1
        

print("la cantidad de ceros es: " , cero)
print("la cantidad de positivos es: " , positivos)
print("la cantidad de negativos es: " , negativos)





