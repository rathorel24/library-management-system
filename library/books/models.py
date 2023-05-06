from django.db import models
from django.utils.translation import gettext_lazy as _
from users.models import User

class InventoryStatus(models.IntegerChoices):
    BORROWED = 1
    RETURNED = 2 


class Book(models.Model):
    name = models.CharField(_("Book Name"),max_length=200)
    author = models.CharField(_("Author"),max_length=200,blank=True,null=True)
    year = models.DateField(_("Date of publication"),blank=True,null=True)


    def __str__(self):
        return f"{self.id} - {self.name}"


class BookBorrowInventory(models.Model):
    book = models.OneToOneField("Book", on_delete=models.CASCADE, related_name="borrow_inventory")
    borrower = models.ForeignKey("users.User", on_delete=models.SET_NULL, related_name="borrowed_books",
                                 blank=True,null=True,verbose_name=_("Borrower_user"))
    status = models.IntegerField(_("Status"),choices=InventoryStatus.choices,default=InventoryStatus.BORROWED)
    borrow_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.id} - {self.book} - {self.borrower}"
