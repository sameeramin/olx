from django.db import models
from django.contrib.auth.models import User


class City(models.Model):
    name = models.CharField(max_length=75)

    class Meta:
        db_table = 'cities'
        verbose_name_plural = 'cities'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=75)

    class Meta:
        db_table = 'categories'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Ad(models.Model):
    title = models.CharField(max_length=75)
    short_description = models.CharField(max_length=150)
    description = models.TextField()
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    address = models.CharField(max_length=75)
    city = models.ForeignKey(City, on_delete=models.RESTRICT)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_sold = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'listings'
        ordering = ('-created_at', )

    def __str__(self):
        return f"{self.title} - Posted by {self.user.username}"


class Image(models.Model):
    ad = models.ForeignKey(Ad, default=None, on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='Image', blank=True)

    class Meta:
        db_table = 'images'

    def __str__(self):
        return self.image.name
