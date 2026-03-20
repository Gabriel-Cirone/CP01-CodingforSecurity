import random

opcoes = {
    1: "Pedra",
    2: "Papel",
    3: "Tesoura",
    4: "Lagarto",
    5: "Spock"
}

# Regras: quem vence + ação
regras = {
    1: {3: "quebra", 4: "esmaga"},       # Pedra
    2: {1: "cobre", 5: "refuta"},        # Papel
    3: {2: "corta", 4: "decapita"},      # Tesoura
    4: {2: "come", 5: "envenena"},       # Lagarto
    5: {1: "vaporiza", 3: "derrete"}     # Spock
}

print("1 = Pedra")
print("2 = Papel")
print("3 = Tesoura")
print("4 = Lagarto")
print("5 = Spock")

jogador = int(input("Escolha uma opção: "))


if jogador < 1 or jogador > 5:
    print("Opção inválida")
else:
    computador = random.randint(1, 5)

    print(f"Você: {opcoes[jogador]}")
    print(f"Computador: {opcoes[computador]}")

    if jogador == computador:
        print("Empate!")

    elif computador in regras[jogador]:
        acao = regras[jogador][computador]
        print(f"{opcoes[jogador]} {acao} {opcoes[computador]} — Você venceu!")

    else:
        acao = regras[computador][jogador]
        print(f"{opcoes[computador]} {acao} {opcoes[jogador]} — Computador venceu!")
