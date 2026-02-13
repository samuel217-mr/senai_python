contador = 0
notas = []

def media(lista):
    total  = 0 
    for i in lista :
     total = total + i 
     return total / len(lista)

    return 

while contador < 3:
    nota  = float ( input(f"informe a nota {contador + 1 }"))  
    notas.append(nota)
    contador += 1 

    print(f"notas : {nota}")

    resultado = media(notas) 
print (f"resultado: {resultado}")
