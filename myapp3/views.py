from django.shortcuts import render, get_object_or_404
from .form import CreateBookForm
from .models import Book
from django.http import HttpResponseRedirect
from django.utils.timezone import now

# Create your views here.


def main_page(request):
    return render(request, 'myapp3/main_page.html', {'timestamp': now().timestamp()})


def add_page(request):
    if request.method == 'POST':
        form = request.POST
        author = form['author']
        title = form['title']
        Book.objects.create(title=title, author=author)
        return HttpResponseRedirect('/myapp3/')
    else:
        return render(request, 'myapp3/add_book_page.html', {'timestamp': now().timestamp()})


def search_page(request):
    if request.method == 'POST':
        form = request.POST
        data = Book.objects.all()
        if form['id'] != "":
            data = data.filter(id=int(form['id']))
        if form['author'] != "":
            data = data.filter(author__icontains=form['author'])
        if form['title'] != "":
            data = data.filter(title__icontains=form['title'])
        return render(request, 'myapp3/search_book_page.html', {'timestamp': now().timestamp(), 'rows': data})
    else:
        return render(request, 'myapp3/search_book_page.html', {'timestamp': now().timestamp(), 'rows': Book.objects.all()})


def update_page(request, id):
    if request.method == 'POST':
        form = request.POST
        if form['action'] == "update":
            record = get_object_or_404(Book, id=id)

            record.title = form['title']
            record.author = form['author']

            record.save()
            return HttpResponseRedirect('/myapp3/search_book/')
        else:
            record = get_object_or_404(Book, id=id)

            record.delete()

            return HttpResponseRedirect('/myapp3/search_book/')
    else:
        data = Book.objects.filter(id=id)
        return render(request, 'myapp3/update_book_page.html', {'id': id, 'title': data[0].title, 'author': data[0].author})


def home(request):
    if request.method == 'POST':
        form = CreateBookForm(request.POST)
        if form.is_valid():
            formdata = form.cleaned_data
            title = formdata['title']
            author = formdata['author']
            Book.objects.create(title=title, author=author)
            return HttpResponseRedirect('/myapp3/success')
    else:
        form = CreateBookForm()
        return render(request, 'myapp3/createbook.html', {'form': form})


def success(request):
    return render(request, 'myapp3/success.html')

