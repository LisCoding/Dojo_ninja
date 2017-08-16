from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Book(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField(default="N/A")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    # There can be many books to one user
    uploader = models.ForeignKey(User, related_name = "uploaded_books")
    #there is a many to many relationship between likes
    # a user can like many books and book can have many likes
    liked_users = models.ManyToManyField(User, related_name="liked_books")
