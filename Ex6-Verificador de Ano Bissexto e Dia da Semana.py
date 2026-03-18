testes = [
    (29, 2, 2024),
    (29, 2, 2023),
    (31, 4, 2025),
    (15, 8, 2025),
    (29, 2, 2000),
    (29, 2, 1900),
    (5, 13, 2025),
    (0, 6, 2025),
]

for dia, mes, ano in testes:
    print(f"Data: {dia:02d}{mes:02d}{ano}")

    # Verificar se é bissexto
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        bissexto = True
        print("Ano bissexto: Sim")
    else:
        bissexto = False
        print("Ano bissexto: Não")

    if mes < 1 or mes > 12:
        print("Data inválida: mês inválido")
    else:
    
        if mes == 2:
            if bissexto:
                dias_mes = 29
            else:
                dias_mes = 28

        elif mes in [4, 6, 9, 11]:
            dias_mes = 30

        else:
            dias_mes = 31

        if dia < 1:
            print("Data inválida: dia inválido")

        elif dia > dias_mes:
            if mes == 2:
                print(f"Data inválida: fevereiro de {ano} tem apenas {dias_mes} dias")
            else:
                print(f"Data inválida: mês {mes} tem apenas {dias_mes} dias")

        else:
            print("Data válida")

    print()  
