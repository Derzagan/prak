import nltk
nltk.download('punkt_tab')

text = "Привет мир. Как дела?"

words = nltk.word_tokenize(text)
print(words)

sentences = nltk.sent_tokenize(text)
print(sentences)