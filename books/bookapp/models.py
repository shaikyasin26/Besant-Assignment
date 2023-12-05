from django.db import models
class Book(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    genre=models.CharField(max_length=20)
    ISBN=models.CharField(max_length=100)
    av_status=models.CharField(max_length=20)
    def __str__(self):
        return self.title
class Library(models.Model):
    ISBM=models.ForeignKey('Book',on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    membership_details=models.TextField(max_length=200)
    def __str__(self):
        return self.name

class Borrow(models.Model):
    book=models.ForeignKey('book', on_delete=models.CASCADE)
    patron=models.CharField(max_length=100)
    borrowing_dt=models.DateTimeField(auto_now=False)
    return_dt=models.DateTimeField(auto_now=False)
    def __str__(self):
        return self.patron


# Create your models here.
