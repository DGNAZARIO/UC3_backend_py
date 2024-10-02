#Exercício 4: Simulador de Dados Financeiros
#Objetivo: Simular o saldo de uma conta com juros compostos usando loops e incrementadores.
#- Descrição: Solicite ao usuário um saldo inicial, a taxa de juros anual e o número de anos.
#Use um loop ‘while’ para simular o aumento do saldo com juros compostos ao longo dos anos e
#imprima o saldo final após o período especificado.

saldo_inicial = float(input("Digite o saldo inicial: "))
taxa_juros = float(input("Digite a taxa de juros anual (em %): ")) / 100
anos = int(input("Digite o número de anos: "))

saldo = saldo_inicial
ano = 0

while ano < anos:
    saldo *= (1 + taxa_juros)
    ano += 1

print(f"O saldo final após {anos} anos é: {saldo:.2f}")
