from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView
from .models import Book



class HomeView(TemplateView):
    template_name = "home.html"

class BookListView(ListView):
    model = Book
    template_name = "book_list.html"
    context_object_name = "books"

class BookDetailView(DetailView):
    model = Book
    template_name = "book_detail.html"
    context_object_name = "book"

class BookcreateView(CreateView):
    model = Book
    fields = "__all__"
    template_name = "book_create.html"
    success_url = '/books'

class BookUpdateView(UpdateView):
    model = Book
    fields = "__all__"
    template_name = "book_update.html"
    success_url = '/books'

class BookDeleteView(DeleteView):
    model = Book
    template_name = "book_delete.html"
    success_url = '/books'