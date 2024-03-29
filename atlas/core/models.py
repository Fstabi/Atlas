"""
Database models.
"""
# import uuid
# import os

# from django.conf import settings
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user."""
        if not email:
            raise ValueError('User must have an email address.')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create and return a new superuser."""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    hearts = models.IntegerField(default=0)
    coins = models.IntegerField(default=0)
    general_score = models.IntegerField(default=0)

    objects = UserManager()

    USERNAME_FIELD = 'email'


class Category(models.Model):
    """Model representing a category."""
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    
class Level(models.Model):
    """Model representing a level in the game."""

    name = models.CharField(max_length=255)
    level_score = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
class BasicChallenge(models.Model):
    name = models.CharField(max_length=100)
    difficulty = models.IntegerField(null=False)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    level_id = models.ForeignKey(Level, on_delete=models.CASCADE)
    score_id =  models.IntegerField() #models.ForeignKey(Score, on_delete=models.CASCADE)

class SimpleChallenge(BasicChallenge): #Lo stesso modello si per Flags, multiple choices -> trovare una naming convention
    photo_link = models.URLField()

class AreaChallenge(BasicChallenge):
    area = models.TextField()
    photo_link = models.URLField()

class CoordinateChallenge(BasicChallenge):
    lat = models.TextField()
    long = models.TextField()
    photo_link = models.URLField()


    def __str__(self):
        return self.name


class Score(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    challenge = models.ForeignKey(BasicChallenge, on_delete=models.CASCADE)
    score = models.IntegerField()

    def __str__(self):
        return f"Score for {self.user.username} on {self.challenge.name}: {self.score}"
