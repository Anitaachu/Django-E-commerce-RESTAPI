from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.title

class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=100, default='John Doe')
    category = models.ForeignKey(Category, related_name='books', null=True, on_delete=models.CASCADE)
    isbn = models.CharField(max_length= 13)
    pages = models.IntegerField()
    price = models.IntegerField()
    quantity = models.IntegerField()
    description = models.TextField(blank=True)
    imageurl = models.URLField(blank=True)
    status = models.BooleanField()
    date_created = models.DateField(auto_now_add=True)


    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title

class Grocery(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='grocery', null=True, on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField()
    imageurl = models.URLField(blank=True)
    status = models.BooleanField()
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return '{} {}'.format(self.product_tag, self.name)
    

CLOTHES_CHOICES = (
    ('T-shirt', 'T-shirt'),
    ('Jeans', 'Jeans'),
    ('Jacket', 'Jacket'),
    ('Dress', 'Dress'),
    ('Shorts', 'Shorts'),

)


CLOTHES_SIZES = (
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
    ('XL', 'Extra lage'))


class Clothing(models.Model):
    clothes = models.CharField(max_length=50, choices=CLOTHES_CHOICES, null=True, blank=True)
    category = models.ForeignKey(Category, related_name='clothing', null=True, on_delete=models.CASCADE)
    color = models.CharField(max_length=50)
    size = models.CharField(max_length=20, choices=CLOTHES_SIZES, null=True, blank=True)
    price = models.IntegerField()
    quantity = models.IntegerField()
    imageurl = models.URLField(blank=True)
    status = models.BooleanField()
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.clothes