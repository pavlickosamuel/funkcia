def translation(text):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    translated = ""
    counter = 0
    while counter < len(text):
        char = text[counter]
        if char in vowels:
            counter += 3
            translated += char
        elif char in consonants:
            counter += 2
            translated += char
        else:
            counter += 1
            translated += char
    return translated
preklad = translation("hieeelalaooo")
print(preklad)

