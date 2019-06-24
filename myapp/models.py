# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Book(models.Model):
    book_name = models.TextField(max_length=50)
    book_number = models.IntegerField()
    author = models.TextField(max_length=50)
    released_date = models.DateField()

    class Meta:
        db_table = "book"

    def __str__(self):
        return self.book_name    
