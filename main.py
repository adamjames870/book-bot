from stats import count_words, count_chars_and_sort

def main():
    PATH_FRANKENSTEIN = "books/frankenstein.txt"
    book_text = get_book_text(PATH_FRANKENSTEIN)
    word_count = count_words(book_text)
    print(f"{word_count} words found in the document")
    char_count = count_chars_and_sort(book_text)
    print(char_count )

def get_book_text(path_to_file):
    file_contents = ""
    with open(path_to_file) as book_file:
        file_contents = book_file.read()
    return file_contents

main()