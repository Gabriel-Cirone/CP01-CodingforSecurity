# Lista de testes
testes = [
    {"salario": 2000.00, "dependentes": 0, "pensao": 0, "idoso": False},
    {"salario": 5000.00, "dependentes": 2, "pensao": 0, "idoso": False},
    {"salario": 8000.00, "dependentes": 1, "pensao": 500, "idoso": False},
    {"salario": 3500.00, "dependentes": 0, "pensao": 0, "idoso": True},
]

# Faixas INSS (limite, taxa)
faixas_inss = [
    (1518.00, 0.075),
    (2793.88, 0.09),
    (4190.83, 0.12),
    (8157.41, 0.14),
]

# Faixas IR
faixas_ir = [
    (2259.20, 0),
    (2826.65, 0.075),
    (3751.05, 0.15),
    (4664.68, 0.225),
    (float("inf"), 0.275),
]

for caso in testes:
    salario = caso["salario"]
    dependentes = caso["dependentes"]
    pensao = caso["pensao"]
    idoso = caso["idoso"]

    print("====================================")
    print("CONTRACHEQUE — Cálculo de IR Mensal")
    print("====================================")
    print(f"Salário bruto:       R$ {salario:.2f}\n")

    # INSS
    inss = 0
    anterior = 0

    for limite, taxa in faixas_inss:
        if salario > anterior:
            base = min(salario, limite) - anterior
            valor = base * taxa
            inss += valor
            print(f"Faixa {taxa*100:.1f}%:      R$ {valor:.2f}")
            anterior = limite

    print(f"(-) INSS total:      R$ {inss:.2f}\n")


    # Deduções
    desc_dep = dependentes * 189.59
    desc_idoso = 1903.98 if idoso else 0

    base = salario - inss - desc_dep - pensao - desc_idoso
    if base < 0:
        base = 0

    print(f"Base de cálculo IR:  R$ {base:.2f}\n")


    # IR
    ir = 0
    anterior = 0

    for limite, taxa in faixas_ir:
        if base > anterior:
            valor_base = min(base, limite) - anterior
            valor = valor_base * taxa
            ir += valor
            print(f"Faixa {taxa*100:.1f}%:      R$ {valor:.2f}")
            anterior = limite

    print(f"\n(-) IR total:        R$ {ir:.2f}")

   
    # Final
 
    liquido = salario - inss - ir

  
    print(f"Salário líquido:     R$ {liquido:.2f}")

  
