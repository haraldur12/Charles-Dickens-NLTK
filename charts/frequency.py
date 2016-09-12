# Import Libraries
import nltk
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.probability import *
import csv

# Set Variables
with open('pickwickpapers.txt', 'r') as file:
    novel_text = file.read().decode('utf8')

file = csv.writer(open('word_frequencies.csv', 'w' ))

novel_tokens = word_tokenize(novel_text)
text = nltk.Text(novel_tokens)

# Load in Stopwords Library / Cleans the text for reliable results
stopwords = stopwords.words('english')

word_set = []

# Define Functions
def normalize_text(text):
    # Work through all the words in text and filter
    for word in text:
        # Check if word is a word, and not punctuation, AND check against stop words
        if word.isalpha() and word.lower() not in stopwords:
            # If it passes the filters, save to word_set
            word_set.append(word.lower())
    return word_set


normalize_text(text)

fd = FreqDist(word_set)
print fd.most_common(200000)
#print fd.hapaxes()
#fd.plot(50,cumulative=False)

# Print results to a CSV file
for key, count in fd.most_common(200000):
    file.writerow([key, count])

fd.plot(100,cumulative=False)