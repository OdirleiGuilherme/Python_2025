salario = float(input("Digite seu salário para verificar aumento anual: "))

porcentagem = 18

aumento = (salario * porcentagem)/100
salario_atualizado = salario+(salario * porcentagem)/100

print(f'Seu salário de R$ {salario:.2f} foi ajustado em {porcentagem}%, aumetando para R$ {salario_atualizado:.2f} '
      f'Tendo um aumento em R$ {aumento:.2f}')