try:
    while True:
        print("Operadores Aritméticos")
        print("-" * 10)

        name = str(input("Digite seu nome: ")) 
        idade = input("Digite sua idade: ")
        cor = input("Digite sua cor favorita: ")
        print(f"Olá {name}, você tem {idade} anos e sua cor favorita é {cor}.")

        # Case sensitivity example: Azul vs azul
        if cor.lower() == "verde":
            print(f"Tambem adoro {cor}")
        elif cor.lower() == "azul":
            print(f"Azul é uma cor muito bonita, {name}!")
        else:
            print(f"Não gosto muito de {cor}, prefiro azul.") 

        Resposta = input("Deseja continuar? (s/n): ").strip().lower()
        if Resposta == 'n':
            break
        elif Resposta != 's':
            print("Resposta inválida. Por favor, digite 's' para sim ou 'n' para não.")
except ValueError:    
    print("Por favor, insira apenas números inteiros.")