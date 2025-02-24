import sys
from stats import count_words, count_characters, sort_dictionary

def get_book_text(file_path):
    content = ""
    with open(file_path) as f:
        content += f.read()
    return content


def print_report(dict, num_words, path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for pair in dict:
        for key in pair:
            if key.isalpha():
                print(f"{key}: {pair[key]}")
    print("============= END ===============")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(path)
    num_words = count_words(text)
    num_characters = count_characters(text)
    sorted_characters = sort_dictionary(num_characters)

    print_report(sorted_characters, num_words, path)


main()


