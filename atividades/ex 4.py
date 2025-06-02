
PopulaçãoMundial = 8090000000

TaxaCrescimento = 0.011


# Exibindo a população estimada para os próximos 5 anos

for ano in range(1, 6):
    CalculoPopulacãoFutura = PopulaçãoMundial * (1 + TaxaCrescimento) ** ano
    print(f"População estimada em {ano} ano(s): {PopulacaoFutura:,.0f}")