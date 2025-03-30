from stats import count_words, count_chars_and_sort
import sys

def main():
    
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    # PATH_FRANKENSTEIN = "books/frankenstein.txt"
    
    path = sys.argv[1]
    book_text = get_book_text(path)
    word_count = count_words(book_text)
    char_count = count_chars_and_sort(book_text)
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    print_char_count(char_count)
    print("============= END ===============")

def get_book_text(path_to_file):
    file_contents = ""
    with open(path_to_file) as book_file:
        file_contents = book_file.read()
    return file_contents

def print_char_count(char_dict):
    for line in char_dict:
        print(f"{line}: {char_dict[line]}")

main()