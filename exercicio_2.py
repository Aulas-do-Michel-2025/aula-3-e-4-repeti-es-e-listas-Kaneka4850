"""
#### Exercício 2 - Filtrando uma lista.

Receba uma lista de input do usuário.

Ele digitará como um texto com os números separados por vígula. Para isso, pode-se utilizar o código disponibilizado que
vai transformar esse texto em lista para você.

Depois imprima uma lista apenas com os números ímpares.

Dica: Crie outra lista e popule ela, a partir da varredura da lista original.

Exemplos:

----------------------------------

Digite a sua lista (separando os números por vírgula): 1, 2, 3, 4, 5
Resposta:
Os números ímpares são [1, 3, 5]
"""

# Código para pegar a lista
# Pede ao usuário uma lista de números separados por vírgula
entrada = input("Digite a sua lista (separando os números por vírgula): ")

# Converte a string em uma lista de inteiros
lista = list(map(int, entrada.split(",")))

# Cria uma lista vazia para guardar os números ímpares
impar = []

# Percorre cada número na lista
for i in lista: 
    # Verifica se o número é ímpar
    if i % 2 != 0:
        # Adiciona o número ímpar à lista
        impar.append(i)

# Mostra os números ímpares encontrados
print(impar)
