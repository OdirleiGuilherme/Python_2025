# programe um aumento de salário, de forma que ele calcule um
# aumento de 15% para um salário de R$750.

salario = 750

porcentagem = 15

aumento = (salario * porcentagem)/100
salario_atualizado = salario+(salario * porcentagem)/100

print(f'Seu salário de R$ {salario:.2f} foi ajustado em {porcentagem}%, aumetando para R$ {salario_atualizado:.2f} '
      f'Tendo um aumento em R$ {aumento:.2f}')