
# Solicita ao usuário que insira um número de 5 dígitos
numero = int(input("Digite um número de 5 dígitos: "))

# Verifica se o número tem exatamente 5 dígitos
if 10000 <= numero <= 99999:
    # Separa os dígitos individualmente
    digito1 = numero // 10000
    digito2 = (numero % 10000) // 1000
    digito3 = (numero % 1000) // 100
    digito4 = (numero % 100) // 10
    digito5 = numero % 10

# Imprime os dígitos, cada um em uma nova linha

    print(digito1)
    print(digito2)
    print(digito3)
    print(digito4)
    print(digito5)
else:
    print("O número digitado não tem exatamente 5 dígitos.")