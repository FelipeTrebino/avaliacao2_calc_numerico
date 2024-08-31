print("\nInterpolação Polinomial - Método de Newton........")
#n = int(input("Insira a quantidade de pontos: "))
qtd_pontos = 3
#while n <= 0:
#    n = int(input("Por favor, a quantidade de pontos deve ser maior que zero.#\nInsira a quantidade de pontos: "))
#x = float(input("Insira o valor de x que você deseja calcular: "))
x = 1.8

print("\nInsira os pontos...................................")
pontos_x = [1, 1.5, 2]
pontos_y = [2, 2.725, 3.414]
d = []
#for i in range(n):
#    ponto_x = float(input(f"Insira o valor de x{i}:"))
#    ponto_y = float(input(f"Insira o valor de y{i}:"))
#    pontos_x.append(ponto_x)
#    pontos_y.append(ponto_y)
m = qtd_pontos - 1
n = qtd_pontos
pointer_y = 0
pointer_x = 1
for j in range(m):
    pointer_x = j + 1
    for i in range(n - 1):
        num = pontos_y[pointer_y + 1] - pontos_y[pointer_y]
        den = pontos_x[pointer_x] - pontos_x[pointer_x - (j + 1)]
        k = []
        pontos_y.append(num / den)
        k.append(num)
        k.append(den)
        k.append(num / den)
        d.append(k)
        pointer_y += 1
    pointer_y += 1
    n -= 1

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
    