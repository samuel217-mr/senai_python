import random 

continuar   =  True
palavrachave = input ( " informe uma palavra ").lower().strip() 
#palavrachave = input ( " informe uma palavra ").lower().strip() 

palavra = ["python","pc","lulu","carro" ]
palavrachave = random.choice(palavra)


digitados = []
acertos  = [] 
erro     = 0 

while continuar:

    senha = ""

    for letra in palavrachave:
        senha += letra if letra in acertos else "."

    print(senha) 

    if senha == palavrachave:
           print (" voce acertou ! ")
    break 
    tentativa = input ("digite uma letra :").lower().strip()

    if tentativa in digitados:
        print("voce ja digitou essa letra")
        continue 
    
    else: 
        digitados += tentativa 
        if tentativa in palavrachave:
            acertos += tentativa 
        else :
            errors += 1 
            print(" voce errou ! ")

print("x==:==\nx : ")
print("x   o " if erro >= 1 else "x" )
print("X  O " if erro >= 1 else "X")
linha2 = ""
if erro == 2:
    linha2 += "   | "
elif erro == 3:
    linha2 += "  \| "
elif erro >=4:
   linha2 += "   \|/ "
   linha3= ""

if erro >=5:
    linha3 = " / "
    linha3 += " / "
elif erro >= 6:
        linha3 = " / \ " 

        linha3 += " / \ "

   

print (" x%s "  %linha3)
print("x\n=============")

if erro == 6:
    print("voce foi inforcado")

    opcao = int(input("deseja continuar ? 1- sim | 2- nao "))
    if (opcao == 2 ):
     continuar = False 
