# Written by students: Guilherme Almeida and Marcos Vinicius

# Storing values 
precos = [4,2,10,1,2]
pesos = [12,1,4,1,2]
peso_total = 15

# Creating helper variables
i = 0
j = 0
aux = []

# Assigning division values to a list
while i in range(len(precos)):
  temp = pesos[i] / precos[i]
  i += 1 
  aux.append(temp)
  
print("A proporção é de: {}".format(aux))
print("\nO melhor custo beneficio é: {}".format(min(aux)) )

# Putting items inside the backpack
melhor_peso = min(aux)
print(melhor_peso)

# i = 0
# while i < len(aux) - 1:
#   if(aux[i] == melhor_peso):
#     precos.pop(i)
#     pesos.pop(i)
      
# print(pesos)
    



  
  
  

