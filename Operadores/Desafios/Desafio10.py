# IF com Laços
# Crie um script que receba um valor numerico e verifique se ele é maior do que o numero anterior.
# Se for maior, imprima "O número é maior que o anterior".
# Se não for, imprima "O número não é maior que o anterior".
# O script deve solicitar o número até que o usuário decida parar.
# Use um laço de repetição para permitir várias entradas de números.
# num_anterior = 10

numeroDaSuaVariavel = int(input("Digite um número: "))

num_anterior = 10

while True:
    if num_anterior > numeroDaSuaVariavel:
        print("O número não é maior que o anterior.")

    if num_anterior == numeroDaSuaVariavel:
        print("O número é igual ao anterior.")
        break
