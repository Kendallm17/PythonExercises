def is_isogram(string):
    palabra = string.lower()
    letras = []

    for c in palabra:
        if c.isalpha():         
            if c in letras:     
                return False
            letras.append(c)

    return True
