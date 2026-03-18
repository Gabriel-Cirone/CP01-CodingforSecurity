testes = [
    {"entrada": 14, "saida": 16, "placa_final": 3, "dia": "quarta"},
    {"entrada": 9,  "saida": 9,  "placa_final": 7, "dia": "sexta"},
    {"entrada": 23, "saida": 2,  "placa_final": 5, "dia": "sabado"},
    {"entrada": 8,  "saida": 12, "placa_final": 4, "dia": "segunda"},
    {"entrada": 20, "saida": 3,  "placa_final": 2, "dia": "segunda"},
]

for caso in testes:
    entrada = caso["entrada"]
    saida = caso["saida"]
    placa = caso["placa_final"]
    dia = caso["dia"]

    print("=== Estacionamento ===")
    print(f"Entrada: {entrada:02d}h | Saída: {saida:02d}h")

    if saida >= entrada:
        horas = saida - entrada
    else:
        horas = (24 - entrada) + saida

    if horas == 0:
        horas = 1

    print(f"Permanência: {horas} hora(s)")

    if horas >= 1:
        total = 10 
        if horas > 1:
            total += (horas - 1) * 5

    print(f"Tarifa base:     R$ {total:.2f}")

    noturno = False
    hora_atual = entrada

    for i in range(horas):
        if hora_atual >= 22 or hora_atual < 6:
            noturno = True
        hora_atual = (hora_atual + 1) % 24

    adicional_noturno = 0
    if noturno:
        adicional_noturno = total * 0.5
        total += adicional_noturno
        print(f"Adicional noturno (50%): R$ {adicional_noturno:.2f}")

    desconto = 0
    if dia == "segunda" and placa % 2 == 0:
        desconto = total * 0.10
        total -= desconto
        print(f"Desconto (10%):  R$ {desconto:.2f}")

    print(f"Total:           R$ {total:.2f}")

    print()
    