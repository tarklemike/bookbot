def get_book_text(file):
    with open(file) as f:
        return f.read()

def word_count(file):
    text = get_book_text(file)
    words = text.split()
    return len(words)
    

def main():
    print(f'{word_count("./books/frankenstein.txt")} words found in the document')

main()