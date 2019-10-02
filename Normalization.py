# Stemming 

from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer



def stemming(word):
    
    ps = PorterStemmer()
    stemmed_words = ps.stem(word)
    return stemmed_words

def lemmatization(word):

    lem = WordNetLemmatizer()
    lem_word = lem.lemmatize(word, "v")
    return lem_word



text = "I am flying better than birds ;)"
tokenized_words = word_tokenize(text)
stemmed_words = []
lem_words = []

for w in tokenized_words:

    stemmed_words.append(stemming(w))
    lem_words.append(lemmatization(w))


print("Tokenize words: ",  tokenized_words)
print("Stemmed words: ", stemmed_words)
print("Lemmatized_words: ", lem_words)