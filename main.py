def main():
    book_path = "books/frankenstein.txt" 
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    character_count = get_char_count_dict(text)
    print(f"{num_words} words found in the document \n character frequency in the text as follows {character_count}") 

def get_char_count_dict(text):
    lower_text = text.lower()
    char_frequency = {}
    for char in lower_text:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1
    return char_frequency

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

if __name__ == "__main__":
    main()