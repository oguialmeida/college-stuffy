# Written by students: Guilherme Almeida and Marcos Vinicius

class No:
     def __init__(self, key, direita, esquerda):
          self.item = key
          self.direita = direita
          self.esquerda = esquerda

class Arvore:
     def __init__(self):
          self.raiz = No(None,None,None)
          self.raiz = None
     
     # Insert an alement into the tree
     def inserir(self, v):
          novo = No(v,None,None) 
          if self.raiz == None:
               self.raiz = novo
          else: 
               atual = self.raiz
               while True:
                    anterior = atual
                    if v <= atual.item: 
                         atual = atual.esquerda
                         if atual == None:
                                anterior.esquerda = novo
                                return
                    else: 
                         atual = atual.direita
                         if atual == None:
                                 anterior.direita = novo
                                 return
     
     # Return to next node (needed for comparison)
     def no_seguinte(self, apaga): 
          paidoseguinte = apaga
          seguinte = apaga
          atual = apaga.direita

          while atual != None: 
               paidoseguinte = seguinte
               seguinte = atual
               atual = atual.esquerda 
               paidoseguinte.esquerda = seguinte.direita 
               seguinte.direita = apaga.direita 
                                        
          return seguinte

    # Remove an element with the help of the above function
     def remover(self, v):
         if self.raiz == None:
               return False 
         atual = self.raiz
         pai = self.raiz
         filho_esquerda = True
    
         while atual.item != v: 
               pai = atual
               if v < atual.item:
                    atual = atual.esquerda
                    filho_esquerda = True 
               else: 
                    atual = atual.direita 
                    filho_esquerda = False 
               if atual == None:
                    return False 

         if atual.esquerda == None and atual.direita == None:
               if atual == self.raiz:
                    self.raiz = None 
               else:
                    if filho_esquerda:
                         pai.esquerda =  None 
                    else:
                         pai.direita = None 

         elif atual.direita == None:
               if atual == self.raiz:
                    self.raiz = atual.esquerda 
               else:
                    if filho_esquerda:
                         pai.esquerda = atual.esquerda 
                    else:
                         pai.direita = atual.esquerda 
         
         elif atual.esquerda == None:
               if atual == self.raiz:
                    self.raiz = atual.direita 
               else:
                    if filho_esquerda:
                         pai.esquerda = atual.direita 
                    else:
                         pai.direita = atual.direita 

         else:
               seguinte = self.no_seguinte(atual)
               if atual == self.raiz:
                    self.raiz = seguinte 
               else:
                    if filho_esquerda:
                         pai.esquerda = seguinte 
                    else:
                         pai.direita = seguinte 
               seguinte.esquerda = atual.esquerda   

         return True

# Calls the desired class
arv = Arvore()
opcao = ()

print('Bem vindo ao sistema persist??ncia de Dados que utiliza ??rvores AVL')
print('\nEscolha uma das op????es abaixo:')

while opcao != 0:
     print('\n1 ??? Inserir um novo elemento na ??rvore AVL') 
     print('\n2 ??? Excluir um elemento da ??rvore')
     print('\n0 ??? Encerrar o programa ')
     opcao = int(input())
     if opcao == 1:
          x = int(input("Informe o valor: "))
          arv.inserir(x)
     elif opcao == 2:
          x = int(input("Informe o valor: "))
          if arv.remover(x) == False:
               print("Valor n??o encontrado na ??rvore")	
     elif opcao == 0:
          break