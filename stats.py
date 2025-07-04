def number_of_words(book_texts):
    return len(book_texts.split())

def count_of_each_char(book_texts):
    book_texts = book_texts.lower()
    char_count = {}
    for c in book_texts:
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1
    return char_count

def sort_on(items):
    return items["num"]

def sort_counts(counts):
    list_of_dicts = []
    for c in counts:
        if c.isalpha():
            list_of_dicts.append({"char": c, "num": counts[c]})
    list_of_dicts.sort(key=sort_on, reverse=True)
    return list_of_dicts

