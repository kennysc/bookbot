
'''
Made this program in the boot.dev course "Build a Bookbot in Python".
The program can read a text file a return the number of words in the file,
as well as the occurence of each lowered alpha character in the file.

Kenny St-Cyr 2025-09-18
'''
import sys
from stats import *

# check that sys.argv as at least one item, item_1 = program,
# item_2 = argument/path
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1) 

def main():
    path = sys.argv[1]
    book = get_book_text(path)
    nbr_words = word_count(book)
    characters = reorder_dict(book)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {nbr_words} total words")
    print("--------- Character Count -------")
    
    for i in characters:
        if i["char"].isalpha():
            print(f"{i["char"]}: {i["num"]}")
    
    print("============= END ===============")

main()