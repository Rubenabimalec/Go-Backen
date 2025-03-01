"""7 reglas de numeros romanos:
1. Si a la derecha de una letra hay otra con igual o menor valor, el valor de esta se suma a la anterior  x =< y
2. La letra I situada delante de la V o la X resta una unidad a V o a X.
3.


"""
def decimal_a_romano(num):
    valores = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"),
        (1, "I")
    ]
    
    resultado = ""
    
    for valor, simbolo in valores:
        while num >= valor:
            resultado += simbolo
            num -= valor
            
    return resultado

# Ejemplo de uso
print(decimal_a_romano(1987))  # "MCMLXXXVII"
