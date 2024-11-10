"""
Use Django signals to automatically create a log entry whenever a new book is added or deleted.
The log should include the book title, author, and the action (create/delete).
"""
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Book

import logging

@receiver(post_save, sender=Book)
def create_log_entry(sender, instance, created, **kwargs):
    if created:
        logging.info(f"Book {instance.title} created by {instance.author.name}")

@receiver(post_delete, sender=Book)
def delete_log_entry(sender, instance, **kwargs):
    logging.info(f"Book {instance.title} deleted by {instance.author.name}")