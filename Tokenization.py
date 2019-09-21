
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


def word_tokenizer(text):
    
    tokenized_word=word_tokenize(text)
    print(tokenized_word)


text = "Hello Mr. Smith, how are you doing today? The weather is great, and city is awesome"

sentence_tokenizer(text)
word_tokenizer(text)