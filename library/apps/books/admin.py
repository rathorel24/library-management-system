from django.contrib import admin
from .models import Book
from .models import BookBorrowInventory

# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','author', 'year',)


@admin.register(BookBorrowInventory)
class BookBorrowInventoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'borrower','status' ,'borrow_date', 'return_date')