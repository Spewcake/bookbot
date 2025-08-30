from stats import word_amount
from stats import char_amount
from stats import split_dict

def get_book_text(fp):
    with open(fp,"r") as f:
        file_contents = f.read()
        return file_contents

book_text = get_book_text("books/frankenstein.txt")
word = word_amount(book_text)
char = char_amount(book_text)
sorted_list = split_dict(char)

def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word} total words")
    print("--------- Character Count -------")
    for entry in sorted_list:
        print(f"{entry["char"]}: {entry["num"]}")
    print("============= END ===============")
main()