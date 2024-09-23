import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

class UserManager(BaseUserManager):

    def get_object_by_public_id(self, public_id):
        try:
            instance = self.get(public_id=public_id)
            return instance
        except (ObjectDoesNotExist, ValueError, TypeError):
            return Http404
    
    def create_user(self, username, email, password, **kwargs):
        if not username:
            raise TypeError('Username is required')
        if not email:
            raise TypeError('Email is required')
        if not password:
            raise TypeError('Password is required for super user')
        user = self.model(username=username, email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_super_user(self, username, email, password, **kwargs):
        if not username:
            raise TypeError('Superusers must have an username')
        if not email:
            raise TypeError('Superusers must have an email')
        if not password:
            raise TypeError('Superusers must have a password')
        user = self.create_user(username, email, password, **kwargs)
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)

        return user


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    public_id = models.UUIDField(unique=True, editable=False, default=uuid.uuid4, db_index=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True, db_index=True)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(blank=True)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self) -> str:
        return f'{self.email}'
    
    @property
    def name(self):
        return f'{self.first_name} {self.last_name}'

