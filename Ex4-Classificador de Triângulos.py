# Lista de testes
testes = [
    (5, 5, 5),    
    (5, 5, 3),    
    (3, 4, 5),    
    (1, 2, 10),   
    (0, 5, 5),    
    (7, 7, 12),   
]

for a, b, c in testes:
    print(f"Lados: {a}, {b}, {c}")

    if a <= 0 or b <= 0 or c <= 0:
        print("Não forma triângulo")

    elif a + b > c and a + c > b and b + c > a:
        
        if a == b and b == c:
            print("Triângulo válido: Equilátero")

        elif a == b or a == c or b == c:
            print("Triângulo válido: Isósceles")

        else:
            print("Triângulo válido: Escaleno")
    else:
        print("Não forma triângulo")

    print()  
