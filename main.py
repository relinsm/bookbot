def count_words(text):
    """Returns the number of words in the given text."""
    words = text.split()
    return len(words)

def count_characters(text):
    """Returns a dictionary with character frequencies in the text."""
    text = text.lower()  # Convert to lowercase
    char_count = {}

    for char in text:
        if char.isalpha():  # Only count alphabetic characters
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

    return char_count

def sort_on(dict):
    """Sorting function to sort by 'num' key in descending order."""
    return dict["num"]

def print_report(file_path, word_count, char_count):
    """Prints the formatted report with word and character counts."""
    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document\n")

    # Convert dictionary to a sorted list
    sorted_chars = [{"char": char, "num": count} for char, count in char_count.items()]
    sorted_chars.sort(reverse=True, key=sort_on)

    for entry in sorted_chars:
        print(f"The '{entry['char']}' character was found {entry['num']} times")

    print("--- End report ---")

def main():
    path_to_file = "books/frankenstein.txt"
    
    with open(path_to_file, "r") as f:
        file_contents = f.read()
    
    word_count = count_words(file_contents)
    char_count = count_characters(file_contents)
    
    print_report(path_to_file, word_count, char_count)

if __name__ == "__main__":
    main()
