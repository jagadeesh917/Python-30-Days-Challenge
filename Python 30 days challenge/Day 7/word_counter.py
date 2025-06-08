from collections import Counter
import string

def count_word_frequency(filename):
    with open(filename, 'r') as file:
        text = file.read().lower()
    words = [word.strip(string.punctuation) for word in text.split()]
    return Counter(words)

# Print column-wise output
frequencies = count_word_frequency('sample.txt')
for word, count in frequencies.items():
    print(f'{word} : {count}')


