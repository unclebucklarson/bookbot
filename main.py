
path = 'books/'
book_name = "frankenstein.txt"

def main():
    with open(path+book_name) as f:
        data = f.read()
    
    # print(data)
    words_in_book = len(return_words_in_string(data))

    chars_in_book = char_count(data)

    print(f"--- Begin report of {path+book_name} ---")

    print(f"{words_in_book} words found in the document\n")

    found_chars = list(chars_in_book)
    found_chars.sort()

    # print(chars_in_book)
    # print(found_chars)
    for char in found_chars:
        print(f"The '{char}' character was found {chars_in_book[char]} times")
   
    print("--- End report ---")


def return_words_in_string(the_string):
   return the_string.split()

def char_count(the_string):
    the_string = the_string.lower()
    char_dict = dict()

    for letter in the_string:
        letter = letter.lower()
        if letter.isalpha():
            if letter not in char_dict.keys():
                char_dict[letter] = 1
            else:
                char_dict[letter] += 1
    
    return char_dict


if __name__ == "__main__":
    main()
