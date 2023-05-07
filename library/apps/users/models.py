from django.db import models

# Create your models here.
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone


class UserRole(models.IntegerChoices):
    LIBRARIAN = 1, "LIBRARIAN"
    MEMBER = 2, "MEMBER"

    
class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)
    

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    first_name = models.CharField(_("First Name"),max_length=50)
    last_name = models.CharField(_("Last Name"),max_length=50,blank=True,null=True)
    role = models.IntegerField(_("Role"),choices=UserRole.choices,default=UserRole.MEMBER)
    is_staff = models.BooleanField(_("Is staff user"),default=False)
    is_active = models.BooleanField(_("Is active ?"),default=True)
    created_at = models.DateTimeField(editable=False)
    modified_at = models.DateTimeField(editable=False)


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.modified_at = timezone.now()
        return super(User, self).save(*args, **kwargs)


    objects = UserManager()

    def __str__(self):
        return f"{self.id} - {self.email}"