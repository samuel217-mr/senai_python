categoria=int(input("informe uma categoria"))
qtd=int(input("informe uma quantidade"))
valor=0
error=False  



if categoria == 1:
     valor= 10.
elif categoria== 2:
     valor= 18.
elif categoria== 3:
     valor= 23.
elif categoria== 4:
     valor= 26.
elif categoria== 5:
     valor= 31.
else:
     error= True 
     print("categoria invalida")
     
if not error :
     print(f"categoria {categoria}\npreco unit : ´{qtd}\ntotal:{valor * qtd}")