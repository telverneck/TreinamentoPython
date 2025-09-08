# Condicionais 

idade = int(input("Digite sua idade: "))
nome = "João"

print(f"Eu tenho {idade} e meu nome é {nome}.")

if idade > 18 and idade < 40:
    print("Você é maior de idade.\n")

elif idade == 18:
    print("Uau! você tem a minha idade.\n")

elif idade >= 40 and idade <= 120:
    print("Você ja é um veterano.\n")

else:
    print("Você é um anciao\n")

