from http.client import HTTPResponse
from multiprocessing import context
from django.shortcuts import render,HttpResponse,redirect
from .models import Book,Auther

def add_app(request):
    context = {
        'book': Book.objects.all
    }
    return render(request , "index.html" ,context)

def form_add(request):
    Book.objects.create(title = request.POST['title'],desc = request.POST['description'] )
    return redirect("/add_book")

def view(request,book_id):
    print('***')
    this_book = Book.objects.get(id=book_id)
    context = {
        'book':Book.objects.get(id=book_id),
        'authers':this_book.authers.all,
        'authers_all':Auther.objects.all,
        'authers_all':Auther.objects.all
    }
    return render(request,'view.html' ,context)

def add_auther(request):
    print("********")
    print(request)
    this_book = Book.objects.get(id=int(request.POST['book_id']))
    this_auther = Auther.objects.get(id=int(request.POST['auth_id']))
    this_book.authers.add(this_auther)
    return redirect("/show/" + request.POST['book_id'])