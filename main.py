import sys
from stats import get_word_count,get_character_count, get_sorted_character_dictionarys

def get_book_text(file):
    with open(file) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    character_count = get_character_count(text)
    character_dictionarys = get_sorted_character_dictionarys(character_count)
    print("============ BOOKBOT ============")
    print(f'Analyzing book found at {book_path}')
    print("----------- Word Count ----------")
    print(f'Found {word_count} total words')
    print("--------- Character Count -------")
    for dictionary in character_dictionarys:
        if dictionary["char"].isalpha():
            print(f'{dictionary["char"]}: {dictionary["num"]}')
    print("============= END ===============")

main()