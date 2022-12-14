def converter():
    while True:
        try:
            print("\nDigite [1] para converter para dolar:")
            print("Digite [2] para converter para real:")
            print("Digite [0] para sair:")
            op = input("")
            result = 0
            if op == '1':
                valor = float(input("Qual o valor que deseja converter? "))
                result = valor / 5.26
                print("O valor em dolar é de: {}".format(round(result, 2)))

            elif op == '2':
                valor = float(input("Qual o valor que deseja converter? "))
                result = valor * 5.26
                print("O valor em reais é de: {}".format(round(result, 2)))

            elif op == '0':
                print("Fim")
                break
            else:
                print("Desculpe, não entendi, poderia repetir?")
        except:
            print("Entrada inválida! Tente novamente")
            
if __name__=="__main__":
    converter()
            
