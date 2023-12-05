from django.contrib import admin
from bookapp.models import Book
admin.site.register(Book)
from bookapp.models import Library
admin.site.register(Library)
from bookapp.models import Borrow
admin.site.register(Borrow)

# Register your models here.
