from django.http import HttpResponse
import replace
from django import forms
from django.shortcuts import render


# Create your views here.

class UserForm(forms.Form):
    SendMeText = forms.CharField()


def index(request):
    if request.method == 'POST':
        my_word = request.POST.get('SendMeText')
        origin = my_word
        return HttpResponse(f"Текст - {origin}  |   Извлеченные слова - {replace.replace(my_word)}")
    else:
        userform = UserForm()
        return render(request, 'index.html', {'form': userform})
