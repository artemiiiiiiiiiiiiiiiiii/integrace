from django.http import HttpResponse
import replace


# Create your views here.

def index(request, my_word):
    return HttpResponse(f"Текст - {my_word}  |   Извлеченные слова - {replace.replace(my_word)}")
