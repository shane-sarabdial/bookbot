from stats import number_of_words, count_of_each_char, sort_counts, sort_on
import sys
def get_book_texts(file_path):
    with open(file_path) as f:
        book_texts = f.read()
    return book_texts


def main ():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    book_texts = get_book_texts(book)
    num_of_words = number_of_words(book_texts)
    count = count_of_each_char(book_texts)
    sort = sort_counts(count)
    print("============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n"
          "----------- Word Count ----------")
    print(f"Found {num_of_words} total words")
    print("--------- Character Count -------")
    for i in sort:
        print(f"{i['char']}: {i['num']}")
    print("============= END ===============")


if __name__ == '__main__':
    main()