import math

def integracao(f, lim_inf, lim_sup, qtd_partes):
    passo = (lim_sup - lim_inf) / qtd_partes
    valores_x = []
    valores_y = []
    valores_x.append(lim_inf)
    valores_y.append(f(lim_inf))
    pont_x = 0
    for i in range(0, qtd_partes):
        x = (valores_x[pont_x] + passo)
        valores_x.append(x)
        pont_x += 1
        y = f(x)
        valores_y.append(y)


    intermediario = 0

    for i in range(1, qtd_partes):
        intermediario += valores_y[i]
        print(f"[{valores_x[i]}, {valores_y[i]}]")

    return (passo / 2)*((f(lim_inf) + f(lim_sup)) + 2 * intermediario)

def f(x):
    return math.exp(x)

if __name__ == "__main__" :
    
    print("Para o exemplo de implementação de Integração Numérica a seguir, será utilizada a f(x) = e^x.")

    qtd_partes = int(input("Insira a quantidade de partes em que você deseja dividir o seu intervalo: "))

    lim_inf = float(input("Insira o limite inferior do intervalo: "))

    lim_sup = float(input("Insira o limite superior do intervalo: "))

    integral = integracao(f, lim_inf, lim_sup, qtd_partes)

    print(f"O resultado da integral é {integral}")