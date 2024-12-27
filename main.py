def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = get_book_words(book_path)
    chars = get_char_numbers(book_path)
    print (f"--- Begin report of {book_path} ---")
    print (f"There are {words} words in this book.\n")
    for char in chars:
        if not char.isalpha():
            continue
        print(f"The '{char}' character was found {chars[char]} times.")

    

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_book_words(path):
    with open(path) as f:
        text = f.read()
        return(len(text.split()))
    
def get_char_numbers(path):
    with open(path) as f:
        text = f.read().lower().replace(" ","")
        final_result = {}
        for char in text:
            if char in final_result:
                final_result[char] += 1
            else:
                final_result[char] = 1
        final_result.pop('\n', None)    
        return dict(sorted(final_result.items()))

main()