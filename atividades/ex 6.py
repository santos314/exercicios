#exercicio 6

peso = float(input("Peso em kg: "))
altura = float(input("Altura em metros: "))

imc = peso / (altura * altura)

print("IMC:", round(imc, 2))