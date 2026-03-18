testes = [
    380,
    1250,
    70,
    15,
    -100,
    0,
]

for valor in testes:
    print(f"=== Saque: R$ {valor} ===")

    if valor <= 0:
        print("Valor inválido")

    elif valor % 10 != 0:
        print("Valor inválido")

    else:
        restante = valor

        ced_200 = restante // 200
        restante = restante % 200

        ced_100 = restante // 100
        restante = restante % 100

        ced_50 = restante // 50
        restante = restante % 50

        ced_20 = restante // 20
        restante = restante % 20

        ced_10 = restante // 10
        restante = restante % 10

        total = ced_200 + ced_100 + ced_50 + ced_20 + ced_10

        print(f"R$ 200: {ced_200} cédula(s)")
        print(f"R$ 100: {ced_100} cédula(s)")
        print(f"R$ 50:  {ced_50} cédula(s)")
        print(f"R$ 20:  {ced_20} cédula(s)")
        print(f"R$ 10:  {ced_10} cédula(s)")
        print(f"Total de cédulas: {total}")

    print()
    