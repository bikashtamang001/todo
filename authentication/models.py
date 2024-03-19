
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager
)
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken

class UserManager(BaseUserManager):
    """
    Django requires that custom users define their own Manager class. By
    inheriting from `BaseUserManager`, we get a lot of the same code used by
    Django to create a `User`. 

    All we have to do is override the `create_user` function which we will use
    to create `User` objects.
    """

    def create_user(self, username, email, password=None, first_name=None,
                    last_name=None):
        """
        Create and return a `User` with an email, username, first_name, last_name
        and password.
        """
        if username is None:
            raise TypeError("Users must have a username")
        if email is None:
            raise TypeError("Users must have an email address")
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name
        )
        user.set_password(password)
        user.save()

        return user
    
    def create_superuser(self, username, email, password):
        """
        Create and return a `User` with superuser (admin) permissions.
        """
        if password is None:
            raise TypeError("Superusers must have a password")
        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user

class User(AbstractBaseUser):
    """
    Class to represent user model
    """
    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(db_index=True, unique=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    # Tells Django that the UserManager class defined above should manage
    # objects of this type.
    def __str__(self):
        """
        Returns a string representation of this `User`.

        This string is used when a `User` is printed in the console.
        """
        return self.username
    
    @property
    def token(self):
        """
        Generates a JSON Web Token that stores this user's instance and has an expiry
        date set to 60 days into the future.
        """
        token = RefreshToken.for_user(self)
        return {
            "refresh": str(token),
            "access": str(token.access_token)
        }
