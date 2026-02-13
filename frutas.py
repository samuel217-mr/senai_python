continuar = True 
lista=[]

while continuar:
    fruta = input("informe uma fruta")
    lista.append(fruta.strip)

    desejacontinuar = input ("deseja continuar?  SIM (S) | NAO (N)")

    if(desejacontinuar.strip().lower()=="n"or
        desejacontinuar.strip().lower()=="nao" or
        desejacontinuar.strip().lower()=="nao "):
        continuar = False 

print(f"a fruta informada:\n{lista}")


