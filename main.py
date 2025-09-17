def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def word_count(text):
    return len(text.split())

def main():
    book = get_book_text("books/frankenstein.txt")
    nbr_words = word_count(book)
    print(f"{nbr_words} words found in the document")

main()