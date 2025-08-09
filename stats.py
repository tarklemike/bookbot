def get_word_count(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    count_dictionary = {}
    for c in text:
        character = c.lower()
        if character in count_dictionary:
            count_dictionary[character] += 1
        else:
            count_dictionary[character] = 1
    return count_dictionary