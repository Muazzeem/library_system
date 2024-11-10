from django.core.cache import cache
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import AuthorSerializer, BookSerializer
from .models import Author, Book

# Create your views here.

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer



class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [SearchFilter]
    ordering_fields = ['author__name', 'genre']

    def get_queryset(self):
        queryset = self.queryset
        author_name = self.request.query_params.get('author_name', None)
        genre = self.request.query_params.get('genre', None)
        publication_after = self.request.query_params.get('publication_after', None)
        publication_before = self.request.query_params.get('publication_before', None)

        if author_name:
            queryset = queryset.filter(author__name=author_name)
        if genre:
            queryset = queryset.filter(genre=genre)
        if publication_after:
            queryset = queryset.filter(publication_date__gte=publication_after)
        if publication_before and publication_after:
            queryset = queryset.filter(publication_date__range=[publication_after, publication_before])
        return queryset

    # def list(self, request, *args, **kwargs):
    #     cache_key = "books_list"
    #     cached_books = cache.get(cache_key)
    #     if cached_books is not None:
    #         return Response(cached_books)
    #     else:
    #         books = self.get_queryset()
    #         cache.set(cache_key, books)
    #         return Response(books)