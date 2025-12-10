from stats import get_num_words, get_character_appearance, sort_dict, get_book_text
import sys


if len(sys.argv) < 2:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)
else:
    path = sys.argv[1]
text = get_book_text(path)
num_words = get_num_words(text)
apperance = sort_dict(get_character_appearance(text))
print('============ BOOKBOT ============')
print(f'Analyzing book found at {path}...')
print('----------- Word Count ----------')
print(f'Found {num_words} total words')
print('--------- Character Count -------')
for k, v in apperance:
    if k.isalpha():
        print(f'{k}: {v}')
print('============= END ===============')