from django.shortcuts import render
# Create your views here.
from .models import Book, Author, BookInstance, Genre

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_genres = Genre.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # Number of books that contain the word 'the' in the title
    num_books_with_word = Book.objects.filter(title__icontains='the').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    
    # Uncomment below to reset counter
    # request.session['num_visits'] = 0
    
    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres' : num_genres,
        'num_books_with_word' : num_books_with_word,
        'num_visits': num_visits,
    }

    # Render/create the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

# part 6
from django.views import generic

class BookListView(generic.ListView):
    model = Book
    paginate_by = 10

class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author
    template_name = 'catalog/author_list.html'
    context_object_name = 'authors'
    paginate_by = 10

class AuthorDetailView(generic.DetailView):
    model = Author