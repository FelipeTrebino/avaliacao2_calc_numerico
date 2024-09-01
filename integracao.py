import math

# Limites de integração: lim_inf (a) e lim_sup (b)
# Quantidade de partes: qtd_partes
# Função a ser integrada: f(x)

def integracao_trapezio(f, lim_inf, lim_sup, qtd_partes):
    passo = (lim_sup - lim_inf) / qtd_partes # Calculo delta
    
    soma = 0
    x = lim_inf
    
    for _ in range(qtd_partes):
        y = passo * (f(x) + f(x + passo)) * 0.5 
        soma += y
        #print(f"[{x}, {y}]")
        x += passo

    return soma

def integracao_simpson(f, lim_inf, lim_sup, qtd_partes):
    passo = (lim_sup - lim_inf) / qtd_partes # Calculo delta
    
    soma = - f(lim_inf) + f(lim_sup) # Os limites não entram na lógica do loop
    # Forma generalizada da 1a regra de simpson, utilizando regra do 1/3
    for i in range(qtd_partes):
        x = lim_inf + i * passo
        if i % 2 == 0:
            y = 2 * f(x)
        else:
            y = 4 * f(x)
        soma += y
    soma = soma 
    
    return soma * 1/3 * passo

def e(x):
    return math.exp(x)

def quadratica(x):
    return x**2

def cubica(x):
    return x**3

def linear(x):
    return 2*x + 3

def seno(x):
    return math.sin(x)

def cosseno(x):
    return math.cos(x)

def logaritmo_natural(x):
    return math.log(x)

if __name__ == "__main__" :
        
    f = None
    qtd_partes = None
    lim_inf = None
    lim_sup = None

    print("Integração Numérica - Método dos Trapézios e Método de Simpson ........")
    
    while f == None:
        print ("Escolha a função que deseja integrar: \n")
        print ("1 - e^x \n2 - x^2 \n3 - x^3 \n4 - 2x + 3 \n5 - sen(x) \n6 - cos(x) \n7 - ln(x) \n") 
        try:
            escolha = int(input("Insira o número correspondente à função: "))
            if escolha == 1:
                f = e
            elif escolha == 2:
                f = quadratica
            elif escolha == 3:
                f = cubica
            elif escolha == 4:
                f = linear
            elif escolha == 5:
                f = seno
            elif escolha == 6:
                f = cosseno
            elif escolha == 7:
                f = logaritmo_natural
            else:
                raise ValueError
        except ValueError:
            print("Escolha inválida.")
            f = None

    print(f"Função escolhida: {f.__name__}")

    while qtd_partes == None:
        try:
            qtd_partes = int(input("Insira a quantidade de partes em que você deseja dividir o seu intervalo: "))
            if qtd_partes <= 0:
                raise ValueError
        except ValueError:
            print("A quantidade de partes deve ser um número inteiro positivo.")
            qtd_partes = None
            
    while lim_inf == None:
        try:
            lim_inf = float(input("Insira o limite inferior do intervalo: "))
        except ValueError:
            print("O limite inferior do intervalo deve ser um número real.")
            lim_inf = None
            
    while lim_sup == None:
        try:
            lim_sup = float(input("Insira o limite superior do intervalo: "))
        except ValueError:
            print("O limite superior do intervalo deve ser um número real.")
            lim_sup = None

    

    integral = integracao_trapezio(f, lim_inf, lim_sup, qtd_partes)

    print(f"O resultado da integral via método do trapézio é {integral}")
    
    integral = integracao_simpson(f, lim_inf, lim_sup, qtd_partes)
    
    print(f"O resultado da integral via método de Simpson  é {integral}")
    