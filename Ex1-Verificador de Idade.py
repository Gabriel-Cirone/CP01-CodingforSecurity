def definidor_de_idade(idade_em_anos: int):
    idade_em_anos = int(idade_em_anos)
 
    if idade_em_anos < 0 or idade_em_anos > 120:
        return "Idade inválida"
    elif idade_em_anos <= 11:
        return "Criança"
    elif idade_em_anos <= 17:
        return "Adolescente"
    elif idade_em_anos <= 59:
        return "Adulto"
    else:
        return "Idoso"
 
 
print(f"faixa etaria: {definidor_de_idade (5)}")
print(f"faixa etaria: {definidor_de_idade(15)}")
print(f"faixa etaria: {definidor_de_idade(25)}")
print(f"faixa etaria: {definidor_de_idade(70)}")
print(definidor_de_idade(-3))
print(definidor_de_idade(150))
