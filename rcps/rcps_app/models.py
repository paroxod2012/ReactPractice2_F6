from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=150, blank=True)
    description = models.CharField(max_length=600, blank=True)
    category = models.ForeignKey('Categories', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Categories(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title

