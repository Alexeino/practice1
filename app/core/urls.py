from django.urls import path
from .views import *
urlpatterns = [
    path('books',BooksAPI.as_view(), name="booklistapi")
]
