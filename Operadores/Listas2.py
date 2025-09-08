numeros = [0, 1, 1, 2, 3, 3, 3, 5, 8, 13, 21]
print("Números: ", numeros)
sem_numeros_repetidos = list(set(numeros))  # Remove números repetidos
print("Números sem repetição: ", sem_numeros_repetidos)

lista_final = []
for numero in numeros:
    if numero not in lista_final:
        lista_final.append(numero)
print("Lista final sem repetição: ", lista_final)