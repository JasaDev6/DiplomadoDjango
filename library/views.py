from datetime import datetime
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Author, Book, User, Loan
from .serializers import AuthorSerializer, BookSerializer, UserSerializer, LoanSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

@api_view(['GET'])
def loans_overdue(request):
    overdue_loans = Loan.objects.filter(return_date__lt=datetime.date.today())
    serializer = LoanSerializer(overdue_loans, many=True)
    return Response(serializer.data)