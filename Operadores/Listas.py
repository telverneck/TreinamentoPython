listaSupermercado = ["pao", "leite", "carne", "verduras", "frutas"]

print("Lista Mercadona: ",listaSupermercado)

print("Tamanho da lista: ", len(listaSupermercado))

print("Item 2: ", listaSupermercado[2])

print("Ultimo item: ", listaSupermercado[-1])

listaSupermercado.append("ovos")    
print("Lista atualizada: ", listaSupermercado)
print("Ultimo item: ", listaSupermercado[-1])
listaSupermercado.remove("carne")
print("Lista atualizada: ", listaSupermercado)
print("Item 2: ", listaSupermercado[2])

listaSupermercado.pop()  # Remove o último item da lista
print("Lista atualizada: ", listaSupermercado)

listaSupermercado.sort()  # Ordena a lista em ordem alfabética
print("Lista ordenada: ", listaSupermercado)

listaSupermercado.index("leite")  # Retorna o índice do item "leite"
print("Índice do item 'leite': ", listaSupermercado.index("leite"))

listaSupermercado.insert(1, "manteiga")  # Insere "manteiga" na posição 1
print("Lista atualizada: ", listaSupermercado)

