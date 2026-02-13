from models.pessoafisica import pessoafisica
from models.pessoafisica import pessoafisica 


match escolhar:
     case 1:
        tiposcliente = int (input ("desejo cadastrar 1 - pessoa fisica: 2 - pessoa juridica "))
        nome = ("INFORME NOME ")
        telefone=("INFORME TELEFONE ")
        cpf =("INFORME CPF ")
        cliente = pessoafisica(nome=nome,telefone=telefone)
        list.append(cliente)
        print("CLIENTE REGISTRADO COM SUSESSO")


        

           





















def main():
    print ("INICIALIZANDO SISTEMA ")   
    LIST = []

    carro  = (2026, "BYD" ,  4  ) 
    motoHonda = (2026 , "BYD",2 )
    list . append(carro)
    list . append(motoHonda)

    for v in list :
       print (f"{v.marca}")

    if __name__ == "__main__":
        main()