def main():
    PATH_FRANKENSTEIN = "books/frankenstein.txt"
    book_text = get_book_text(PATH_FRANKENSTEIN)
    word_count = count_words(book_text)
    print(f"{word_count} words found in the document")

def get_book_text(path_to_file):
    file_contents = ""
    with open(path_to_file) as book_file:
        file_contents = book_file.read()
    return file_contents

def count_words(text_to_count):
    words = text_to_count.split()
    return len(words)

main()