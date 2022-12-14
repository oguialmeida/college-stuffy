# Escrito por: Guilherme Almeida
# OBS: No uso do Quick Sort a contagem é através de uma mensagem chamada "Trocou de lugar"

# Biblioteca usada para gerar números aletórios
import random

# Biblioteca usada para contar o tempo de execução
import time

# Escolhe o tamanho do vetor
def tamanho_vetor():
    op = int(input("\nDigite[1] para 5 \nDigite[2] para 10 \nDigite[3] para 15\n"))

    if op == 1:
        tamanho = 5

    elif op == 2:
        tamanho = 10

    elif op == 3:
        tamanho = 15

    return tamanho

# Escolhe números aletórios entre 1 e 100 e preenche o vetor
def preenche_vetor():
    saida = []
    saida = random.choices(range(100), k = tamanho_vetor())
    return saida

# Função responsável pelo bubble sort
def bubble_sort(vetor):
    count = 0
    tamanho = len(vetor)
    for i in range(tamanho - 1):
            for j in range (tamanho -i - 1):
                if vetor[j] > vetor[j + 1]:
                    vetor[j], vetor[j + 1] = vetor[j + 1], vetor[j]
                    count+=1
    print(f"Trocas relazidas: {count}")
    return vetor

# Função responsável pelo quick sort
def quick_sort(vetor):
    if len(vetor) <= 1:
        return vetor
    pivot = vetor[0]
    equal = [x for x in vetor if x == pivot]
    lesser = [x for x in vetor if x < pivot]
    greater = [x for x in vetor if x > pivot]

    print("Trocou de lugar!")

    return quick_sort(lesser) + equal + quick_sort(greater)

# Escolhe o algoritmo de ordenação e o executa
def fazer_ordenacao():
    opcao = int(input("\nDigite[1] para fazer um BubbleSort \nDigite[2] para fazer um QuickSort\n"))
    vetor = preenche_vetor()

    # Implementação do bubble sort
    if opcao == 1:
        inicio = time.time()
        tipo_sort = bubble_sort(vetor)
        nome_sort = "Bubble Sort"
        fim = time.time()

    # Implementação do quick sort
    elif opcao == 2:
        inicio = time.time()
        tipo_sort = quick_sort(vetor)
        nome_sort = "Quick Sort"
        fim = time.time()

    print(f"Vetor ordenado com {nome_sort}: {tipo_sort}")
    print("Tempo de execução: %f" % float(fim - inicio))

# Define uma função principal para que o script seja executado na ordem correta
if __name__ == "__main__":
    fazer_ordenacao()
