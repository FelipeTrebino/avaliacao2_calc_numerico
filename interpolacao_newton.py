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
    
    erro = maior_valor_da_diferenca * np.prod([np.abs(x - pontos_x[j]) for j in range(n-1)]) # Cálculo do erro
    
    return ponto, erro, ordens    
    
if __name__ == "__main__" :

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
        except Exception:
            print("\nEntrada Inválida, tente novamente")


    print("\nPontos Selecionados...........................")
    for i in range(len(pontos_x)):
        print(f"Ponto {i + 1} = [{pontos_x[i]}, {pontos_y[i]}]")

    x = None

    while(x == None):
        try:
            x = float(input("Insira o valor de x que você deseja calcular: "))
        except Exception:
            print("\nValor inválido")
            x = None

    p, erro, ordens = newton(x, pontos_x, pontos_y)
        
    print("\nImprimindo as diferenças....................")
    for i in range(len(ordens)):
        print(f"ordem {i} = {ordens[i]}")

    print("\nImprimindo o resultado final....................")
    print(f"O valor de P({x}) é {p}, o erro estimado é {erro}.")

    
    