import re


def replace(my_word):
    a = re.findall(r'\bй\w*', my_word)
    a = re.sub(r'\bй', r'и', my_word, flags=re.UNICODE)
    return a


