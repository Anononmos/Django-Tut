from django.shortcuts import render
from django.views import generic
from .models import Book, Author, BookInstance, Genre

# Create your views here.

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects

    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available Books (status='a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    num_authors = Author.objects.count()    # all() is implied

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_books': num_books, 
        'num_instances': num_instances, 
        'num_instances_available': num_instances_available, 
        'num_authors': num_authors, 
        'num_visits': num_visits, 
    }

    # Render the HTML template index.html with the data in the context variable

    return render(request, 'index.html', context=context)


class BookListView(generic.ListView):
    model = Book
    paginate_by = 10


class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10


class AuthorDetailView(generic.DetailView):
    model = Author