import nltk
from nltk.corpus import stopwords
from nltk import word_tokenize


with open('taleoftwocities.txt', 'r') as file:
    novel_text = file.read().decode('utf8')

novel_tokens = word_tokenize(novel_text)
text = nltk.Text(novel_tokens)

stopwords = stopwords.words('english')

word_set = []
def normalize_text(text):
    # Work through all the words in text and filter
    for word in text:
        # Check if word is a word, and not punctuation, AND check against stop words
        if word.isalpha() and word.lower() not in stopwords:
            # If it passes the filters, save to word_set
            word_set.append(word.lower())
    return word_set

normalize_text(text)

total = len(text)
unique = len(set(text))

print "Total count of all the tokens is: ", total
print "Total count of the unique tokens is: ", unique

