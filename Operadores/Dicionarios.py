# json - Testes de API

pessoa = {
    "nome": "João",
    "idade": 30,
    "cidade": "Porto",
    "profissão": "Tester/QA",
    "hobbies": ["Programar", "Ler", "Ciclismo"],
    "contato": {
        "email": "telmo@gmail.com",
        "telefone": "123456789"
    }
}

# print(pessoa)
print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print("Cidade:", pessoa["cidade"])      

pessoa["idade"] += 8  # Incrementa a idade em 8 anos
print("Idade atualizada:", pessoa["idade"])


