testes = [
    (80.00,  "nao"),
    (200.00, "nao"),
    (200.00, "sim"),
    (450.00, "nao"),
    (1000.00, "sim"),
]

for valor, vip in testes:
    print("=== Resumo da Compra ===")
    print(f"Valor original:  R$ {valor:.2f}")

    if valor <= 100:
        desconto_base = 0
        porcentagem = 0

    elif valor <= 300:
        desconto_base = valor * 0.10
        porcentagem = 10

    elif valor <= 500:
        desconto_base = valor * 0.15
        porcentagem = 15

    else:
        desconto_base = valor * 0.20
        porcentagem = 20

    print(f"Desconto ({porcentagem}%):  R$ {desconto_base:.2f}")

    if vip == "sim":
        desconto_vip = valor * 0.05
        print(f"Desconto VIP (5%): R$ {desconto_vip:.2f}")
    else:
        desconto_vip = 0

    valor_final = valor - desconto_base - desconto_vip
    print(f"Valor final:     R$ {valor_final:.2f}")

    print()  # separação entre testes
    