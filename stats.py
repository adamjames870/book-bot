
def count_words(text_to_count):
    words = text_to_count.split()
    return len(words)

def count_characters(text_to_count):
    characters = {}
    text_to_count = text_to_count.lower()
    for char in text_to_count:
        current_count = 0
        try:
            current_count = characters[char]
        except KeyError as e:
            pass
        characters[char] = current_count + 1
    return characters

def count_chars_and_sort(text_to_count):
    unsort_dict = count_characters(text_to_count)
    return unsort_dict