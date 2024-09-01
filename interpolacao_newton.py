import numpy as np

def newton(x, pontos_x, pontos_y):
    
    if len(pontos_x) != len(pontos_y):
        raise ValueError("Os vetores pontos_x e pontos_y devem ter o mesmo comprimento.")
    
    ordens = [] # Vetor das diferenças divididas
    
    n = len(pontos_x) # Quantidade de pontos
    
    maior_valor_da_diferenca = np.max(np.abs(pontos_y)) # Maior valor absoluto da diferença
    
    for i in range(n):
        ordem = []
        for j in range(n - i):
            if i == 0:
                ordem.append(pontos_y[j]) # Ordem 0
            else:
                temp = (ordens[i-1][j + 1] - ordens[i-1][j])/(pontos_x[j + i] - pontos_x[j])
                
                if(np.abs(temp) > maior_valor_da_diferenca):
                    maior_valor_da_diferenca = temp # Obter maior valor da diferença para calcular erro posteriormente
                
                ordem.append(temp) # Ordem i > 0
        
        ordens.append(ordem)
      
    ponto = ordens[0][0] # Valor de y interpolado em x  
        
    for i in range(1,n,1):
        dif = ordens[i][0] # Diferença na ordem i (parte de cima da diagonal)
        dif *= np.prod([x - pontos_x[j] for j in range(i)]) # Multiplicação das diferenças em x (x - x0)(x - x1)...(x - xi-1)
        ponto += dif
    
    erro = maior_valor_da_diferenca * np.prod([np.abs(x - pontos_x[j]) for j in range(n)]) # Cálculo do erro
    
    return ponto, erro, ordens
    
"""    

    print("\nImprimindo os resultados dos cálculos....................")
    print("\t  y\t        x\t Resultado")
    for linha in d:
        print("[ ", end="")
        for coluna in linha:
            print(coluna, end="  ")
        print("]")

    ordem = 0
    i = ordem
    print("\nImprimindo as diferenças....................")
    while ordem < qtd_pontos - 1:
        dif = d[i][2]
        print(f"d{ordem} = {dif}")
        ordem += 1
        i += qtd_pontos - ordem

    ordem = 1
    i = qtd_pontos - ordem
    p = pontos_y[0] + d[0][2] * (x - pontos_x[0])
    while ordem < qtd_pontos - 1:
        aux = d[i][2]
        for j in range(ordem + 1):
            aux *= (x - pontos_x[j])
        p -= aux
        ordem += 1
        i += qtd_pontos - ordem

    print("\nImprimindo o resultado final....................")
    print(f"O valor de P({x}) é {p}.")
    """
    
    
if __name__ == "__main__" :

    pontos_x = [0,1,2,3]
    pontos_y = [32,47,65,92]
    ponto, erro, ordens = newton(1.8, pontos_x, pontos_y)

    print(ponto, erro)

    """

    print("\nInterpolação Polinomial - Método de Newton........")

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

    
        

    print("\nImprimindo o resultado final....................")
    print(f"O valor de P({x}) é {p}.")
    
    """