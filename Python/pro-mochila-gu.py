# Written by students: Guilherme Almeida and Marcos Vinicius

peso = 15
itens_dict = {12 : 4, 2 : 2, 4 : 10,  1 : 2, 1 : 1 }

for item in itens_dict:
    if(item <= peso):
        peso -= item
        print('\nAdicionado na mochila')
        print(f"{item} -> {itens_dict[item]}")