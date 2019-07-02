from django.shortcuts import render
from .models import Author, Book

# Create your views here.

def mainPage(request):
    books_list = Book.objects.all()
    context = {
        "books": books_list
    }
    return render(request=request, template_name="index.html", context=context)
