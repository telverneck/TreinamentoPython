print("Operadores Aritméticos")
print("-" * 10)

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
cor = input("Digite sua cor favorita: ")
print(f"Olá {nome}, você tem {idade} anos e sua cor favorita é {cor}.")

# Case sensitivity example: Azul vs azul
if cor.lower() == "verde":
    print(f"Tambem adoro {cor}")
elif cor.lower() == "azul":
    print(f"Azul é uma cor muito bonita, {nome}!")
else:
    print(f"Não gosto muito de {cor}, prefiro azul.") 