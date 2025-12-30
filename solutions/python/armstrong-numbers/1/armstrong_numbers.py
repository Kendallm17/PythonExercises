def is_armstrong_number(number):
    s = str(number)
    longitud = len(s)
    suma = 0

    for i in range(longitud):
        digito = int(s[i])
        suma += digito ** longitud

    return suma == number

