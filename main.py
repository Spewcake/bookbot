import sys
from stats import word_amount
from stats import char_amount
from stats import split_dict
from stats import get_book_text

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else: 
        book_text = get_book_text(sys.argv[1])
        word = word_amount(book_text)
        char = char_amount(book_text)
        sorted_list = split_dict(char)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {word} total words")
        print("--------- Character Count -------")
        for entry in sorted_list:
            print(f"{entry["char"]}: {entry["num"]}")
        print("============= END ===============")
main()