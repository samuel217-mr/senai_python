categoria = int(input(" INFORME UMA CATEGORIA "))
qtd=  int(input(" INFORME QUANTIDADE     "))
valor= 0 
error  = False

match categoria:# escolha   
     case 1:
       valor = 10
     case 2:
       valor = 20
     case 3:
      valor = 30 
     case 4:
      valor = 40
     case _:
       valor = error 

       error = True 
       print ("CATEGORIA INVALIDA ")

       if not error :

       


      
    
