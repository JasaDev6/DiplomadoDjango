from django.contrib import admin
from .models import Author, Book, User, Loan

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(User)
admin.site.register(Loan)
