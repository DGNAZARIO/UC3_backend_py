#Exercício 3: Controle de Formatação de Números Decimais
#Objetivo: Criar um programa que formate números decimais.
#- Descrição: Peça ao usuário para inserir um número flutuante e o
#número de casas decimais desejado. Use f-strings para formatar o
#número com o número de casas decimais especificado e exiba o resultado.

numero = float(input("Digite um número flutuante: "))
casas_decimais = int(input("Digite o número de casas decimais desejado: "))

resultado = f"{numero:.{casas_decimais}f}"

print(f"Número formatado: {resultado}")
