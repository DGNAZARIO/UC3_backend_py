#Escrever um script que identifique números primos em um intervalo.
#- Descrição: Use um loop ‘for’ para iterar de 2 até um número ( N )
#fornecido pelo usuário e dentro do loop, use outro loop para verificar
#se o número atual é primo. Imprima cada número primo encontrado.

def n_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Solicita ao usuário para inserir um número
N = int(input("Digite um número: "))

print(f"Números primos de 2 até {N}:")
for num in range(2, N + 1):
    if n_primo(num):
        print(num)
