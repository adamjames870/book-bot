
def count_words(text_to_count):
    words = text_to_count.split()
    return len(words)

def count_characters(text_to_count):
    characters = {}
    text_to_count = text_to_count.lower()
    for char in text_to_count:
        if not is_ignorable(char):
            current_count = 0
            try:
                current_count = characters[char]
            except KeyError as e:
                pass
            characters[char] = current_count + 1
    return characters

def is_ignorable(char):
    # IGNORABLE_CHARS = [" ", "\n", ":", ",", ".", "?", ";", ":", "“", "”", "!", "-", "'", "_", "—", "*", "1", "2", "3"]
    return not char.isalpha()

def count_chars_and_sort(text_to_count):
    unsorted_dict = count_characters(text_to_count)
    sorted_dict = {key: value for key, value in sorted(unsorted_dict.items(), key=lambda item: item[1], reverse=True)}
    return sorted_dict