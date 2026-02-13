from cliente import CLIENTE 
from  endereco import ENDERECO

def main():
  print("INICIANDO SISTEMA") 

  cliente = cliente ("luis","neto")
  cliente2= cliente ("joao","luiz")
  cliente3= cliente("maria","carvalho")

  
  print(f"nome do client{cliente.nomecompleto()}")
  print(f"nome do client:{cliente2.nomecompleto()}")
  print(f"nome do client:{cliente3.nomecompleto()}")
  

  if __name__ == " __main__ " :
    main()