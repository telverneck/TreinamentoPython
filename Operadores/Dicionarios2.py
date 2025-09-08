alunas = {
    "Ana": 18,
    "Bruna": 17,
    "Carla": 20,
    "Daniela": 16
}

print("Dicionário original:", alunas)
print("Alunos aprovados (nota > 16):")
for nome, nota in alunas.items():
    if nota > 16:
        print(f"{nome}: {nota}")



print("Nota da Ana:", alunas.get("Ana", "Aluna não encontrado"))
print("Nota da Daniela:", alunas.get("Daniela", "Aluna não encontrado"))
print("Nota da Daniela:", alunas.get("Fabiana", "Aluna não encontrado"))




alunas.clear()
print("Dicionário após clear():", alunas)