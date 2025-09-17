from stats import *

def main():
    book = get_book_text("books/frankenstein.txt")
    nbr_words = word_count(book)
    characters = char_count(book)
    print(f"{nbr_words} words found in the document")
    print(characters)

main()