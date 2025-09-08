# LAÇOS DE REPETIÇÃO
# Estruturas de repetição permitem executar um bloco de código várias vezes.

# Uso do For deve ser preferido quando o número de iterações é conhecido.
# Exemplo: Repetir 5 vezes
# Uso do While deve ser preferido quando o número de iterações não é conhecido.
# Exemplo: Repetir até que uma condição seja atendida

while True:

    idade = int(input("Digite sua idade: "))
    nome = "João"

    print(f"Eu tenho {idade} e meu nome é {nome}.")

    if idade > 18 and idade < 40:
        print("Você é maior de idade.\n")
    
    elif idade < 18:
        print("Você é menor de idade.\n")

    elif idade == 18:
        print("Uau! você tem a minha idade.\n")

    elif idade >= 40 and idade <= 120:
        print("Você ja é um veterano.\n")

    else:
        print("Você é um anciao\n")

    if idade == 0:
        print("Saindo do loop.")
        break
print("Fim do loop.")
