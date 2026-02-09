salario=float(input("informe seu salario"))
base=salario 
imposto=base
imposto=0

if base > 300: 
  imposto += imposto + (base-300) * 0.35
  base=300

if base > 1000:
 imposto += imposto  (base - 1000) * 0.20 
 base=1000

 print(f"salario {salario}\nimposto a pagar:´{imposto}")
 print(f"Imposto a pagar: R$ {imposto:.2f}")
 
 


