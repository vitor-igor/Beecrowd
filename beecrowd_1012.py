def area_quadrado(lado: float) -> float:
    """
    Calcula a área de um quadrado.

    Parâmetro:
    - lado (float): Medida do lado do quadrado.

    Retorno:
    - float: Valor da área do quadrado.
    """
    return lado ** 2

def area_retangulo(base: float, altura: float) -> float:
    """
    Calcula a área de um retângulo.

    Parâmetro:
    - base (float): Medida da base do retângulo.
    - altura (float): Medida da altura do retângulo.

    Retorno:
    - float: Valor da área do retângulo.
    """
    return base * altura

def area_triangulo(base: float, altura: float) -> float:
    """
    Calcula a área de um triângulo.

    Parâmetro:
    - base (float): Medida da base do triângulo.
    - altura (float): Medida da altura do triângulo.

    Retorno:
    - float: Valor da área do triângulo.
    """
    return area_retangulo(base, altura) / 2

def area_trapezio(base_maior: float, base_menor: float, altura: float) -> float:
    """
    Calcula a área de um trapézio.

    Parâmetro:
    - base_maior (float): Medida da base maior do trapézio.
    - base_menor (float): Medida da base menor do trapézio.
    - altura (float): Medida da altura do trapézio.

    Retorno:
    - float: Valor da área do trapézio.
    """
    base = base_maior + base_menor 
    return area_triangulo(base, altura)

def area_circulo(raio: float) -> float:
    """
    Calcula a área de um círculo.

    Parâmetro:
    - raio (float): Medida do raio do círculo.

    Retorno:
    - float: Valor da área do círculo.
    """
    pi = 3.14159
    return pi * raio ** 2

num1, num2, num3 = input().split()

num1 = float(num1)
num2 = float(num2)
num3 = float(num3)

# Cálculo das áreas:
triangulo = area_triangulo(num1, num3)
circulo = area_circulo(num3)
trapezio = area_trapezio(num1, num2, num3)
quadrado = area_quadrado(num2)
retangulo = area_retangulo(num1, num2)

print(f"TRIANGULO: {triangulo:.3f}")
print(f"CIRCULO: {circulo:.3f}")
print(f"TRAPEZIO: {trapezio:.3f}")
print(f"QUADRADO: {quadrado:.3f}")
print(f"RETANGULO: {retangulo:.3f}")