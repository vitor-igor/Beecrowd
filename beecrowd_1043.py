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

ladoA, ladoB, ladoC = input().split()

ladoA = float(ladoA)
ladoB = float(ladoB)
ladoC = float(ladoC)

if ((ladoA + ladoB) > ladoC) and ((ladoA + ladoC) > ladoB) and (ladoB + ladoC) > ladoA:
    perimetro = ladoA + ladoB + ladoC
    print(f"Perimetro = {perimetro:.1f}")
else:
    area = area_trapezio(ladoA, ladoB, ladoC)
    print(f"Area = {area:.1f}")