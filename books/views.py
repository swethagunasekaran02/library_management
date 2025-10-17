
# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm
from django.http import HttpResponse
from books.models import Author
Author.objects.all()  
Author.objects.create(name="J.K. Rowling")
Author.objects.create(name="George R. R. Martin")
Author.objects.create(name="Agatha Christie")



# List all books
def book_list(request):
    books = Book.objects.select_related('author').all()
    print(books)
    return render(request, 'books/books_list.html', {'books': books})


# View book details
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/books_detail.html', {'book': book})

# Create new book
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books:book_list')
    else:
        form = BookForm()
    return render(request, 'books/books_form.html', {'form': form, 'title': 'Add New Book'})

# Edit existing book
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('books:book_detail', pk=book.pk)
    else:
        form = BookForm(instance=book)
    return render(request, 'books/books_form.html', {'form': form, 'title': 'Edit Book'})

# Delete book
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('books:book_list')
    return render(request, 'books/books_delete.html', {'book': book})


