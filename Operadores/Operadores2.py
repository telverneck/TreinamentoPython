print("Operadores Aritméticos")
print("-" * 10)

try:
    numero = int(input("Digite um número: "))
    numero2 = int(input("Digite outro número: "))
    soma = int(numero) - int(numero2)

    print(f"O calculo de {numero} - {numero2} = {soma}")
except ValueError:
    print("Por favor, insira apenas números inteiros.")