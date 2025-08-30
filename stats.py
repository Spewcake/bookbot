def get_book_text(fp):
    with open(fp,"r") as f:
        file_contents = f.read()
        return file_contents

def word_amount(b):
    words = b.split()
    num_words = len(words)
    return num_words

def char_amount(b):
    lower_char = b.lower()
    characters = {}
    for c in lower_char:
        if c not in characters:
            characters[c] = 1
        else: characters[c] += 1
        
    return characters

def sort_on(items):
    return items["num"]

def split_dict(dict):
    dict_list = []
    for key in dict:
        if key.isalpha():
            key = {"char": key, "num": dict[key]}
            dict_list.append(key)
    
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list