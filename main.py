frase=input("Ingrese la palabra: ")
def changediccionario(lista):
    L1=list(lista.lower())
    cont = 0
    for i in range(len(L1)):
        for j in range(i,len(L1)):
            if (L1[i]==L1[j]):
                cont = cont + 1
    return cont
print(changediccionario(frase))

print("Estoy acá")