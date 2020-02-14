from django.shortcuts import render, redirect
from .models import Book, Author


def index(request):
    context = {
        'all_books': Book.objects.all()
    }
    return render(request, 'index.html', context)


def authors(request):
    context = {
        'all_authors': Author.objects.all()
    }
    return render(request, 'authors.html', context)


def addBook(request):
    Book.objects.create(title=request.POST['title'], desc=request.POST['desc'])
    print("Book added!")
    return redirect('/')


def addAuthor(request):
    Author.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'])
    print("Author added!")
    return redirect('/authors')


def viewAuthor(request, number):
    context = {
        'author_on_page': Author.objects.get(id=number),
        'all_books': Book.objects.all()
    }
    return render(request, 'view_author_page.html', context)


def viewBook(request, number):
    context = {
        'book_on_page': Book.objects.get(id=number),
        'all_authors': Author.objects.all()
    }
    return render(request, 'view_book_page.html', context)


def addAuthorToBook(request, number):
    book_to_add = Book.objects.get(id=number)
    author_to_add = Author.objects.get(id=request.POST['author_id'])
    book_to_add.authors.add(author_to_add)
    return redirect(f'/view_book/{number}')


def addBookToAuthor(request, number):
    author_to_add = Author.objects.get(id=number)
    book_to_add = Book.objects.get(id=request.POST['book_id'])
    book_to_add.authors.add(author_to_add)
    return redirect(f'/view_author/{number}')

