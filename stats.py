from collections import Counter

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def get_num_words(text):
    return len(text.split())

def get_character_appearance(text):
    return dict(Counter(text.lower()))

def sort_dict(apperance):
    sorted_dict = sorted(apperance.items(), reverse=True, key=lambda x: x[1])
    return sorted_dict