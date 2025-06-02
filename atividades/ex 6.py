peso = 78
altura = 1.85

# Cálculo do IMC
imc = peso / (altura ** 2)
print(f"Seu IMC é: {imc:.2f}")

# Classificação do IMC
classificacao = (
    "Abaixo do peso" if imc < 18.5 else
    "Peso normal" if imc < 25 else
    "Sobrepeso" if imc < 30 else
    "Obesidade grau 1" if imc < 35 else
    "Obesidade grau 2" if imc < 40 else
    "Obesidade grau 3 (obesidade mórbida)"
)

print(f"Classificação: {classificacao}")