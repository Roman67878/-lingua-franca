import nltk
from nltk.tokenize import word_tokenize
from collections import Counter

with open('../grafikk/Herzen.txt', 'r') as file:
    text_for_tokenize = file.read()


def nltk_tokenize(text):
    token_text = nltk.word_tokenize(text, language='russian')
    with open('tokenize file.txt', 'w') as token_file:
        for i in token_text:
            token_file.write(i + ' | ')
    return token_file


def tokenize_split(text):
    token_text = text.split(' ')
    with open('tokenize split.txt', 'w') as token_file:
        for i in token_text:
            token_file.write(i + ' | ')
    return token_file


print(len(list(text_for_tokenize)))
print(sum(Counter(text_for_tokenize).values()))

