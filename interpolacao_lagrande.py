print("\nInterpolação Polinomial - Método de Lagrange........")
n = int(input("Insira a quantidade de pontos: "))
while n <= 0:
    n = int(input("Por favor, a quantidade de pontos deve ser maior que zero.\nInsira a quantidade de pontos: "))
x = float(input("Insira o valor de x que você deseja calcular: "))

print("\nInsira os pontos...................................")
pontos_x = []
pontos_y = []
Lagrange = []
for i in range(n):
    ponto_x = float(input(f"Insira o valor de x{i}:"))
    ponto_y = float(input(f"Insira o valor de y{i}:"))
    pontos_x.append(ponto_x)
    pontos_y.append(ponto_y)

print("\nImprimindo os valores...........................")
for i in range(n):
    print(f"Ponto {i + 1} = [{pontos_x[i]}, {pontos_y[i]}]")

for j in range(n):
    acc_num = 1
    acc_den = 1
    for i in range(n):
        if i != j:
            num = (x - pontos_x[i])
            acc_num *= num
            den = (pontos_x[j] - pontos_x[i])
            acc_den *= den
    l = acc_num / acc_den
    Lagrange.append(l)

print("\nImprimindo os valores de Lagrange...............")
for i in range(n):
    print(f"O valor de L{i} é {Lagrange[i]}")

p = 0
for i in range(n):
    p += pontos_y[i] * Lagrange[i]

print("\nImprimindo o resultado final....................")
print(f"O valor de P({x}) é {p}.")