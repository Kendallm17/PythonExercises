def response(hey_bob):
    texto = hey_bob.strip()

    if not texto:
        return "Fine. Be that way!"

    tiene_letras = any(c.isalpha() for c in texto)
    es_grito = tiene_letras and texto.isupper()
    es_pregunta = texto.endswith('?')

    if es_grito and es_pregunta:
        return "Calm down, I know what I'm doing!"

    if es_grito:
        return "Whoa, chill out!"

    if es_pregunta:
        return "Sure."

    return "Whatever."
