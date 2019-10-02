# Stemming 

from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize


ps = PorterStemmer()
stemmed_words = []
text = "I am flying better than birds ;)"
tokenized_words = word_tokenize(text)

for w in tokenized_words:

    stemmed_words.append(ps.stem(w))

print("Tokenize words",  tokenized_words)
print("Stemmed words", stemmed_words)