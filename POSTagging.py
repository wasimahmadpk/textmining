from nltk.tokenize import word_tokenize
import nltk


def pos_tagging(word):

    postag_word = nltk.pos_tag(word)
    return postag_word


text = "I fly better than all birds :)"

tokenized_words = word_tokenize(text)
postag_words = pos_tagging(tokenized_words)

print("tokenized_words: ", tokenized_words)
print("POS tagged words: ", postag_words)