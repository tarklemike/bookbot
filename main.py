from stats import get_word_count
from stats import get_character_count

def get_book_text(file):
    with open(file) as f:
        return f.read()

def main():
    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    character_count = get_character_count(text)
    print(f'{word_count} words found in the document', character_count)

main()