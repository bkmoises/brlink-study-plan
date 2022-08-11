lista = []
i = 0

while True:
    try:
        while i < 2:
            lista.append(float(input("Digite um número: ")))
            i += 1
        resultado = lista[0] / lista[1]
    except ValueError:
            print("Valor Invalido!")
    except ZeroDivisionError:
            print("O valor não pode ser divido por 0")
    except IndexError:
            print("Posição não encontrada")
    except KeyboardInterrupt:
            print("Execução Interrompida")
    else:
        print(f"O resultado é: {resultado}")
        break
