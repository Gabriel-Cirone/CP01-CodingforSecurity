peso = float(input("Digite o peso em kg: "))
altura = float(input("Digite a altura em metros: "))

imc = peso / (altura * altura)

if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc <= 25:
    classificacao = "Peso normal"
elif imc <= 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obesidade"

print(f"Peso: {peso} kg | Altura: {altura}")
print(f"IMC: {imc:.2f} - {classificacao}")
