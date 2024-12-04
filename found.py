text = "The quick brown fox jumps over the lazy fox and sees another fox"
word_to_find = "fox"

def wordIndexFounder(word_to_find, text):
    words = text.split()
    indices = []
    for index, word in enumerate(words):
        if word == word_to_find:
            indices.append(index)
    if indices:
        print(f"The word '{word_to_find}' is found at indices: {indices}")
    else:
        print(f"The word '{word_to_find}' is not in the list.")

wordIndexFounder(word_to_find, text)