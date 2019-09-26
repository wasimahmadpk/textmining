
""""
Tokenization
Tokenization is the first step in text analytics. The process of breaking down a text paragraph into smaller chunks such as words or sentence is called Tokenization. Token is a single entity that is building blocks for sentence or paragraph.

Sentence Tokenization
Sentence tokenizer breaks text paragraph into sentences.
"""


from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize


def sentence_tokenizer(text):

    tokenized_text = sent_tokenize(text)
    print(tokenized_text)
    return tokenized_text


def word_tokenizer(text):
    
    tokenized_word=word_tokenize(text)
    print(tokenized_word)
    return tokenized_word

def freq_dist(tokenized_word):

    from nltk.probability import FreqDist
    import matplotlib.pyplot as plt

    fdist = FreqDist(tokenized_word)
    print(fdist)
    print(fdist.most_common(2))

    fdist.plot(30, cumulative=False)
    plt.show()


def remove_stop_words(tokenized_sent):

    from nltk.corpus import stopwords
    stop_words = set(stopwords.words("english"))
    print(stop_words)

    filtered_sent = []
    for w in tokenized_sent:
        if w not in stop_words:
            print(w)
            filtered_sent.append(w)
    print("Tokenized Sentence:", tokenized_sent)
    print("Filterd Sentence:", filtered_sent)


text = "Hello Mr. Smith, how are you doing today? The weather is great, and city is awesome and my mood is amazing!"

tsent = sentence_tokenizer(text)
tword = word_tokenizer(text)
freq_dist(tword)
remove_stop_words(tword)
