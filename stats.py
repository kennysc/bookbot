def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def word_count(text):
    return len(text.split())

def char_count(text):
    lower_case = text.lower().split()
    char_dict = {}
    for word in lower_case:
        for letter in word:
            char_dict[letter] = char_dict.get(letter, 0)
            char_dict[letter] += 1
    return char_dict