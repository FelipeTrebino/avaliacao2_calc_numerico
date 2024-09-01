
def lagrange(x, pontos_x, ponto_y):

    n = len(pontos_x) # Quantidade de pontos

    op_lagrange = [] # Vetor dos operadores de Lagrange
    
    for j in range(n):
        l = 1 # Operador de lagrange n
        for i in range(n):
            if i != j:
                #Multiplicação das diferenças
                l *= (x - pontos_x[i])/(pontos_x[j] - pontos_x[i])  
        Lagrange.append(l)

    p = 0 # ponto y em x na função descrita pelos pontos
    for i in range(n):
        p += pontos_y[i] * Lagrange[i]

    return op_lagrange, p

if __name__ == "__main__" :

    print("\nInterpolação Polinomial - Método de Lagrange........")

    pontos_x = []
    pontos_y = []

    print("\nInsira os pontos...................................")

    while(True):
        try:
            i = len(pontos_x)
            ponto_x = float(input(f"Insira o valor de x{i}:"))
            ponto_y = float(input(f"Insira o valor de y{i}:"))
            pontos_x.append(ponto_x)
            pontos_y.append(ponto_y)
            if len(pontos_x) > 2 :
                continuar = input("Quer inserir mais pontos? 's' para sim, qualquer outra coisa para não")
                if continuar == "s":
                    continue

                break
        except TypeError:
            printf("Entrada Inválida, tente novamente")


    printf("Pontos Selecionados...........................")
    for i in range(len(pontos_x)):
        print(f"Ponto {i + 1} = [{pontos_x[i]}, {pontos_y[i]}]")

    x = None

    while(x == None):
        try:
            x = float(input("Insira o valor de x que você deseja calcular: "))
        except TypeError:
            printf("Valor inválido")
            x = None

    operadores, p = lagrange(x, pontos_x, ponto_y)

    print("\nImprimindo os operadores de Lagrange...............")

    for i in range(operadores):
        print(f"O valor de L{i} é {operadores[i]}")

    print("\nImprimindo o resultado final....................")
    print(f"O valor de P({x}) é {p}.")

