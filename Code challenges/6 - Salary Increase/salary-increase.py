salario = int(input()) 

if salario <= 600.00: 
    percentual = 0.17  
     
elif salario >= 600.01 and salario <=900.00:
    percentual = 0.13    
     
elif salario >= 900.01 and salario <=1500.00: 
    percentual = 0.12   

elif salario >= 1500.01 and salario <=2000.00: 
    percentual = 0.10
    
else: percentual = 0.05

novo_salario = (salario * (percentual + 1))
reajuste = (novo_salario - salario)

p = int(percentual * 100)

print(f"Novo salario: {(novo_salario):.2f}\n Reajuste ganho: {reajuste:.2f}\n Em percentual: {p} %".replace(".","."))