text = input("Enter a sentence: ")

print(f"Аналіз тексту: {text}")

words = text.split(" ")
sentences = text.split(".")

print(words)
print(sentences)

import math

count = len(sentences)
word_count = len(words)

if count > 0:
    avarage_words_per_sentence = word_count / count
else:
    avarage_words_per_sentence = 0

print(f"Кількість речень: {count}")
print(f"Кількість слів: {word_count}")
print(f"Середня кількість слів у реченні: {math.ceil(avarage_words_per_sentence)}")
