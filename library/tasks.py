from celery import shared_task
from datetime import datetime
from django.utils import timezone
from .models import Book

@shared_task
def archive_old_books():
    ten_days_ago = timezone.now() - datetime.timedelta(days=365 * 10)
    books_to_archive = Book.objects.filter(publication_date__lt=ten_days_ago, is_archived=False)

    # Archive the books

    for book in books_to_archive:
        book.is_archived = True
        book.save()