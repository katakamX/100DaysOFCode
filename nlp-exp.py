import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.chunk import ne_chunk
from nltk import pos_tag
from nltk.corpus import wordnet
from nltk.tree import Tree
import matplotlib.pyplot as plt

# Download required NLTK data files
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('wordnet')

# Example text
text = "John Smith, a software engineer at Google, visited New York last week."

# 1. Stemming and Lemmatization
print("=== Stemming and Lemmatization ===")
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

tokens = word_tokenize(text)

print("\nStemming:")
for token in tokens:
    print(f"{token} -> {stemmer.stem(token)}")

print("\nLemmatization:")
for token in tokens:
    print(f"{token} -> {lemmatizer.lemmatize(token)}")

# 2. Chunking
print("\n=== Chunking ===")
sent = sent_tokenize(text)[0]
words = word_tokenize(sent)
tagged = pos_tag(words)

# Define a simple NP chunk grammar
chunk_grammar = "NP: {<DT>?<JJ>*<NN|NNP>+}"
chunk_parser = nltk.RegexpParser(chunk_grammar)
chunked = chunk_parser.parse(tagged)

print("Chunked structure:")
print(chunked)
chunked.draw()  # Opens a window to visualize the chunks

# 3. Named Entity Recognition (NER)
print("\n=== Named Entity Recognition ===")
ner_tree = ne_chunk(tagged)

# Print named entities
for subtree in ner_tree:
    if isinstance(subtree, Tree):
        entity_name = " ".join([token for token, pos in subtree.leaves()])
        entity_type = subtree.label()
        print(f"{entity_name} ({entity_type})")

# Visualize NER Tree
ner_tree.draw()  # Opens a window to visualize the NER tree
