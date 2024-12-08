from django.db import models
from django.core.exceptions import ValidationError
import datetime


# Modelo de autor
class Author(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.name


# Modelo de libro
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)

    # Validación personalizada para verificar que la fecha de publicación no sea en el futuro
    def clean(self):
        if self.publication_date > datetime.date.today():
            raise ValidationError("La fecha de publicación no puede ser en el futuro.")

    def __str__(self):
        return self.title


# Modelo de usuario
class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    # Validación personalizada para asegurarse de que el email contenga 'example.com'
    def clean(self):
        if "example.com" not in self.email:
            raise ValidationError("El correo electrónico debe pertenecer al dominio 'example.com'.")

    def __str__(self):
        return self.username


# Modelo de préstamo
class Loan(models.Model):
    user = models.ForeignKey(User, related_name='loans', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name='loans', on_delete=models.CASCADE)
    loan_date = models.DateField()
    return_date = models.DateField()

    # Validación personalizada para asegurar que la fecha de retorno no sea antes de la fecha de préstamo
    def clean(self):
        if self.return_date < self.loan_date:
            raise ValidationError("La fecha de retorno no puede ser antes de la fecha de préstamo.")

    def __str__(self):
        return f'{self.book.title} - {self.user.username}'
