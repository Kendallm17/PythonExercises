def is_pangram(sentence):
    sentence = sentence.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for letra in alphabet:
        if letra not in sentence:
            return False

    return True

