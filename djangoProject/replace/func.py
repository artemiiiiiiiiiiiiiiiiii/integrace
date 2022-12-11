import re


def replace(my_word):
    a = re.findall(r'\bй\w*', my_word)
    a = re.sub(r'\bй', r'и', str(a), flags=re.UNICODE)
    a = re.findall(r'\bи\w*', a)
    return a

