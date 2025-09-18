def get_book_text(filepath):
    # using "with" with open() will open the file ans close it neatly
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

# Helper function to return the value of a dictionary key to help sort a list
# of dict
def sort_on(items):
    return items["num"]

def reorder_dict(text):
    listed = []
    unordered_dict = char_count(text)
    
    # Create a list of dicts where each dict as a character key associated to a
    # number (count) value
    for i in unordered_dict:
        pair = {"char": i, "num": unordered_dict[i]}
        listed.append(pair)
    
    # use the .sort() method of lists to sort using the "num" value returned by
    # the helper function "sort_on"
    listed.sort(reverse=True, key=sort_on)
    return listed
    
