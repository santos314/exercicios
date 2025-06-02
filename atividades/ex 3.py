# Constante para o valor de pi

PI = 3.14159


# Entrada do usuário

raio = int(input("Digite o raio do círculo (inteiro): "))


# Cálculos

diametro = 2 * raio
circunferencia = 2 * PI * raio
area = PI * (raio **2)

# Exibindo os resultados

print("Diâmetro:", diametro)
print("Circunferência:", circunferencia)
print("Área:", area)