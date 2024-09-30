#Criar uma função que calcule o fatorial de um número dado.

#- Descrição: Peça ao usuário para inserir um número e use uma
#função para calcular e retornar o fatorial desse número. O fatorial
#de um número não negativo ( n ), denotado por ( n! ), é o produto de
#todos os números positivos menores ou iguais a ( n ).

def fatorial(n):
    if n < 0:
        return "O fatorial não está definido para números negativos."
    elif n == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado

numero = int(input("Digite um número não negativo: "))
resultado = fatorial(numero)
print(f"O fatorial de {numero} é {resultado}.")
