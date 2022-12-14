# Fatorial de 5, 10 e 15

def painel_selecao():
    op = int(input("\nDigite[1] para 5 \nDigite[2] para 10 \nDigite[3] para 15\n"))

    resultado=1
    count=1

    if op == 1:
        while count <= 5:
            resultado *= count
            count += 1
        print(f"Fatorial do número: {resultado}")

    elif op == 2:
        while count <= 10:
            resultado *= count
            count += 1
        print(f"Fatorial do número: {resultado}")

    elif op == 3:
        while count <= 15:
            resultado *= count
            count += 1
        print(f"Fatorial do número: {resultado}")

if __name__ == "__main__":
    painel_selecao()