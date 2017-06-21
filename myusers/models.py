from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.db import models
from mycompanies.models import Company
from rest_framework.authtoken.models import Token
from core import signals


class UserManager(BaseUserManager):

    def create_user(self, username, email=None, password=None):
        if not username:
            raise ValueError('Login must necessarily be specified')
        
        user = self.model(
            username=username,              
        )
        if email:
            user.email=UserManager.normalize_email(email),
        user.set_password(password)
        user.save(using=self._db)

        Token.objects.create(user=user)
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(username, email, password)
        user.is_admin = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(
        'User name',
        max_length=75,
        unique=True,
        db_index=True   
    )
    email = models.EmailField(
        'E-mail',
        max_length=255,
        db_index=True,
        null=True,
        blank=True
    )
    firstname = models.CharField(
        'First name',
        max_length=40,
        null=True,
        blank=True
    )
    lastname = models.CharField(
        'Last name',
        max_length=40,
        null=True,
        blank=True
    )
    middlename = models.CharField(
        'Middle name',
        max_length=40,
        null=True,
        blank=True
    )
    date_of_birth = models.DateField(
        'Date of birth',
        null=True,
        blank=True
    )
    register_date = models.DateField(
        'Register date',
        auto_now_add=True
    )
    is_active = models.BooleanField(
        'Is active',
        default=False
    )
    is_admin = models.BooleanField(
        'Admin',
        default=False
    )
    is_staff = models.BooleanField(
        'Administrator',
        default=True
    )
    company = models.ForeignKey(
        Company,
        null=True,
        blank=True,
    )
    is_company = models.BooleanField(
        'Company',
        default=False,
    )
    activation_key = models.CharField(max_length=40, null=True)
    key_expires = models.DateTimeField(null=True)

    # Этот метод обязательно должен быть определён
    def get_full_name(self):
        return self.username

    # Требуется для админки
    @property
    def is_staff(self):
        return self.is_admin

    def get_short_name(self):
        return self.username

    def __str__(self):
        return self.username

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        db_table = 'users'