import nltk
import pymorphy3
from nltk.corpus import stopwords

from tokens_task.tokenizee import nltk_tokenize
from nltk.stem.snowball import SnowballStemmer

with open('../grafikk/Herzen.txt', 'r') as file:
    text_for_lemmatize = file.read()


def clean_isalpha(text):
    filtered_text = ''.join(char for char in text if char.isalpha() or char.isspace())
    with open('isalpha1.txt', 'w') as clean_file:
        clean_file.write(filtered_text)
    return clean_file


def stop_words_nltk(text):
    token_text = nltk.word_tokenize(text)
    stopwordz = nltk.corpus.stopwords.words('russian')
    filtered_text = ''.join([word for word in token_text if word.lower() not in stopwordz])
    with open('without_stopwordz.txt', 'w') as clean_file:
        clean_file.write(filtered_text)
    return clean_file


def stemm_nltk(text):
    token_text = nltk.word_tokenize(text)
    stemmer = SnowballStemmer("russian")
    stemmed_text = ''.join([stemmer.stem(word) for word in token_text])
    with open('stemmed.txt', 'w') as clean_file:
        clean_file.write(stemmed_text)
    return clean_file


def lemma_pymorph(text):
    morph = pymorphy3.MorphAnalyzer(lang="ru")
    token_text = nltk.word_tokenize(text)
    lemmed_text = ''.join([morph.parse(word)[0].normal_form for word in token_text])
    with open('lemmed.txt', 'w') as clean_file:
        clean_file.write(lemmed_text)
    return clean_file
    return lemmed_text


lemma_pymorph(text=text_for_lemmatize)
