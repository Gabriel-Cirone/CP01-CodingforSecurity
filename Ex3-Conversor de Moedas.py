# Cotações fixas
cotacoes = {
    "dolar": 5.15,
    "euro": 5.55,
    "libra": 6.45
}

print("=== Conversor de Moedas ===")
print("1 - Real → Dólar")
print("2 - Real → Euro")
print("3 - Real → Libra")

opcao = int(input("Escolha uma opção: "))

if opcao < 1 or opcao > 3:
    print("Opção inválida")
else:
    valor = float(input("Digite o valor em reais: R$ "))

    if valor < 0:
        print("Valor inválido")
    else:
        if opcao == 1:
            convertido = valor / cotacoes["dolar"]
            print(f"Valor em dólar: US$ {convertido:.2f}")

        elif opcao == 2:
            convertido = valor / cotacoes["euro"]
            print(f"Valor em euro: € {convertido:.2f}")

        elif opcao == 3:
            convertido = valor / cotacoes["libra"]
            print(f"Valor em libra: £ {convertido:.2f}")
