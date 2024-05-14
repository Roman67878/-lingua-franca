from collections import Counter
import matplotlib.pyplot as plt
from nltk.draw import dispersion_plot
from nltk import word_tokenize, Text
import pymorphy3


with open('Herzen.txt', 'r') as file:
    text_for_graffiti = file.read()


def graffiti(text):
    text = text.split()
    word_count = Counter(text)
    word_count = word_count.most_common(10)
    plt.plot([word for word, count in word_count], [count for word, count in word_count])
    plt.show()


def most_freq(text):
    text = text.split()
    words = []
    for i in range(len(text)):
        if text[i] not in words:
            words.append(text[i])
        if len(words) == 10:
            break
    dispersion_plot(text, words)
    plt.show()


def gram(text):
    text = text.split()
    morph = pymorphy3.MorphAnalyzer()
    gram_info = [morph.parse(word)[0].tag.POS for word in text]
    with open("gram_text.txt", "w", encoding="utf-8") as clean:
        for i in range(len(gram_info)):
            if gram_info[i] is None:
                continue
            clean.write(gram_info[i])
            clean.write(" ")
    return gram_info


def gram_graffiti(text):
    new_text = gram(text)
    word_count = Counter(new_text)
    word_count = word_count.most_common(10)
    plt.plot([word for word, count in word_count], [count for word, count in word_count])
    plt.show()


def test_methods(text):
    tokens = word_tokenize(text)
    text_obj = Text(tokens)
    sim_word = text_obj.similar("император")
    com_word = text_obj.common_contexts(["отец", "мой"])
    coll_word = text_obj.collocations()


test_methods(text=text_for_graffiti)



