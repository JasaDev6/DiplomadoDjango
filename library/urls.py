from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, BookViewSet, UserViewSet, LoanViewSet, loans_overdue

router = DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)
router.register(r'users', UserViewSet)
router.register(r'loans', LoanViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/loans-overdue/', loans_overdue, name='loans-overdue'),
]
