from django.db import models

class Replacer:
    def __init__(self, text, result):
        self.text = text
        self.result = result
