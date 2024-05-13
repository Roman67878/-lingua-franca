import matplotlib as plt
from collections import Counter
import pymorphy2

from nltk.stem.snowball import SnowballStemmer
import nltk
from nltk.draw import dispersion_plot

with open('Herzen.txt', 'r') as file:
    text_for_graffiti = file.read()


def graffiti(text):
    token_text = nltk.word_tokenize(text)
    stemmer = SnowballStemmer("russian")
    stemmed_text = ''.join([stemmer.stem(word) for word in token_text])
    chast_words = Counter(stemmed_text).most_common(20)
    words, freq = zip(*chast_words)




dispersion_plot(text=text_for_graffiti, words=['Natalie'])
plt.show()

