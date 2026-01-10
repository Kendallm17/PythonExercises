def consonantes_iniciales(palabra):
    palabra = palabra.lower()
    vocales = "aeiou"
    grupo = ""

    for letra in palabra:
        if letra.isalpha() and letra not in vocales:
            grupo += letra
        else:
            break

    return grupo
    
def consonantes_iniciales_con_qu(palabra):
    palabra = palabra.lower()
    vocales = "aeiou"
    grupo = ""
    i = 0

    while i < len(palabra):
        if palabra[i] == "q" and i + 1 < len(palabra) and palabra[i + 1] == "u":
            grupo += "qu"
            i += 2
        elif palabra[i].isalpha() and palabra[i] not in vocales:
            grupo += palabra[i]
            i += 1
        else:
            break

    return grupo
    
def consonantes_hasta_y(palabra):
    palabra = palabra.lower()
    grupo = ""

    for letra in palabra:
        if letra != "y" and letra not in "aeiou":
            grupo += letra
        else:
            break

   
    if len(grupo) < len(palabra) and palabra[len(grupo)] == "y":
        return grupo
    return ""

    
def translate_word(palabra):
    palabra = palabra.lower()

    if palabra[0] in "aeiou" or palabra.startswith("xr") or palabra.startswith("yt"):
        return palabra + "ay"

    grupo = consonantes_iniciales_con_qu(palabra)
    if "qu" in grupo:
        resto = palabra[len(grupo):]
        return resto + grupo + "ay"

    grupo = consonantes_hasta_y(palabra)
    if grupo:
        resto = palabra[len(grupo):]
        return resto + grupo + "ay"

    grupo = consonantes_iniciales(palabra)
    resto = palabra[len(grupo):]
    return resto + grupo + "ay"

def translate(text):
    palabras = text.split()
    resultado = []

    for p in palabras:
        resultado.append(translate_word(p))

    return " ".join(resultado)


    
        
    

        
