from django.db import models
from django.utils.text import slugify
from django.urls import reverse

# chaining custom qs, eg: Product.objects.all().active()
class ProductQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

#custom modelmanager qs, eg: Product.objects.active()
class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)
    def active(self):
        return self.get_queryset().filter(active=True)


class Product(models.Model):
    slug = models.SlugField(null=True, blank=True, unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='media/upload/', null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=0, default=200)
    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    
    objects = ProductManager()

    def __str__(self):
        return self.name
    
    @property
    def title(self):
        return self.name

    def save(self):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save()

    def get_absolute_url(self):
        return reverse("products:product_detail", kwargs={"slug": self.slug})
    
    
    
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    content = models.TextField()
