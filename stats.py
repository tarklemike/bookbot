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

def get_sorted_character_dictionarys(count_dictionary):
    character_dictionarys =  []
    for key, value in count_dictionary.items():
        character_dictionarys.append({"char": key, "num": value})
    character_dictionarys.sort(reverse=True, key=lambda item: item["num"])
    return character_dictionarys