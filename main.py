def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars = get_num_chars(text)
    print(f"--- Begin report of {book_path}\n\n")
    print(f"{num_words} words found in the document")
    for i in num_chars.keys():
        print(f"The {i} was found {num_chars[i]} times")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_num_chars(text):
    text = text.lower()
    return {char: text.count(char) for char in set(text)}
    


main()