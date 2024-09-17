import time
start_time = time.time()
def main():
    book_path = "books/frankenstein.txt" 
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = get_char_count_dict(text)
    char_dict_list = make_dict_list(char_count)
    sorted_list = dict_list_sort(char_dict_list)
    
    print(f"\n--- Begin report of {book_path} ---\n{num_words} words found in the document\n")
    for dictionary in sorted_list:
        print(f"The '{ dictionary['name'] }' character was found {dictionary['num']} times")
    print("--- End report ---")
    end_time = time.time()
    print(f"time it took to process {end_time - start_time} in seconds")

# A function that sorts the list of dictionaries by "num"
def dict_list_sort (list):
    return sorted(list, reverse=True, key=sort_on)


# a list of dictionaries from the char count dictionary
def make_dict_list(dictonary):
    dict_list = []
    for key in dictonary:
        dict_list.append({"name": key, "num":dictonary[key]})
    return dict_list
    

#a helper function that takes a dictionary and returns the value of "num" 
def sort_on(dict):
    return dict["num"]

# Function to get alphabet lowercase character frequency count in a text
def get_char_count_dict(text):
    lower_text = text.lower()
    char_frequency = {}
    for char in lower_text:
        if char in char_frequency:
            char_frequency[char] += 1
        elif char.isalpha():
            char_frequency[char] = 1
    return char_frequency


# Function to get the number of words in the text
def get_num_words(text):
    words = text.split()
    return len(words)


# Function to read the book text from a file
def get_book_text(path):
    with open(path) as f:
        return f.read()


# Run the main function when script is executed
if __name__ == "__main__":
    main()