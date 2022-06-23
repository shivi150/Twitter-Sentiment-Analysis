from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

example_text="Hello there, How are you? I am fine how you are?"

stop_words = set(stopwords.words("english"))

print(stop_words)

words = word_tokenize(example_text)

filtered_sentence = []

for w in words:
    if w not in stop_words:
        filtered_sentence.append(w)

print(filtered_sentence)

filtered_sentence = [w for w in words if w not in stop_words]
print(filtered_sentence)

print(sent_tokenize(example_text))

print(word_tokenize(example_text))


from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps=PorterStemmer()

example_words = ["python","pythoner","pythoning","pythoned","pythonly"]

for w in example_words:
    print(ps.stem(w))


new_text = "It is very important to be pythonly while you are pythoning with python. All pythoners have pythoned poorly at once."
words = word_tokenize(new_text)
for w in words:
    print(ps.stem(w))

    
