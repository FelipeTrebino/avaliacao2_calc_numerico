def lagrange(x, pontos_x, pontos_y):

    if len(pontos_x) != len(pontos_y):
        raise ValueError("Os vetores pontos_x e pontos_y devem ter o mesmo comprimento.")

    n = len(pontos_x) # Quantidade de pontos

    op_lagrange = [] # Vetor dos operadores de Lagrange
    
    for j in range(n):
        l = 1 # Operador de lagrange para o termo j
        for i in range(n):
            if i != j:
                #Multiplicação das diferenças
                l *= (x - pontos_x[i])/(pontos_x[j] - pontos_x[i])  
        op_lagrange.append(l)

    p = 0 # valro de y interpolado em x
    for i in range(n):
        p += pontos_y[i] * op_lagrange[i]

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
            if len(pontos_x) >= 2 :
                continuar = input("Quer inserir mais pontos? 's' para sim, qualquer outra coisa para não: ")
                if continuar == "s":
                    continue

                break
        except TypeError:
            print("\nEntrada Inválida, tente novamente")


    print("\nPontos Selecionados...........................")
    for i in range(len(pontos_x)):
        print(f"Ponto {i + 1} = [{pontos_x[i]}, {pontos_y[i]}]")

    x = None

    while(x == None):
        try:
            x = float(input("Insira o valor de x que você deseja calcular: "))
        except TypeError:
            print("\nValor inválido")
            x = None

    operadores, p = lagrange(x, pontos_x, pontos_y)

    print("\nImprimindo os operadores de Lagrange...............")

    for i in range(len(operadores)):
        print(f"O valor de L{i} é {operadores[i]}")

    print("\nImprimindo o resultado final....................")
    print(f"O valor de P({x}) é {p}.")

