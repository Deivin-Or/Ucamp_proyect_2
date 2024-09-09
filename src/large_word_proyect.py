
def word_lengths(sentence):
    words = sentence.split()
    lengths = [len(word) for word in words]
    return lengths

sentence = "El programa calcula la longitud de cada palabra en una frase"
result = word_lengths(sentence)
print(result)
