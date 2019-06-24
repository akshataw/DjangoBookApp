# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from models import Book
# Create your views here.

def hello(request):
    text = """<h1>Welcome to Django Application!!!</h1>"""
    return HttpResponse(text)

def hello_name(request, myname):
    my_name = "Welcome %s"%myname
    return HttpResponse(my_name)

def all_books(request):
    books = Book.objects.all()
    res = 'Printing all Book netries in the Database: <br>'

    for elt in books:
        res += "<h2>" + elt.book_name + "</h2>" + "&nbsp &nbsp - written by " + elt.author + "<br>"

    return HttpResponse(res)

def get_book(request, bookId):
    book = Book.objects.get(id=bookId)
    text = "Displaying book: %s"%book
    return HttpResponse(text)
