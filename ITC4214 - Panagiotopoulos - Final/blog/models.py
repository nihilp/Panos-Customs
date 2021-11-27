from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey
from phonenumber_field.modelfields import PhoneNumberField


def user_directory_path(instance, filename):
    return 'users/avatars/{0}/{1}'.format(instance.id, filename)


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ProductionCompany(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.name} "

class Motorcycles(models.Model):

    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    
    name = models.CharField(max_length=10)
    company = models.ForeignKey(ProductionCompany, on_delete=models.SET_NULL, null=True, related_name="production_company", blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="category", blank=True)
    capacity = models.IntegerField(null=True, blank=True)
    sold = models.BooleanField(default=False)
    image = models.ImageField(upload_to=user_directory_path, default='motorcycles/default.jpg') 
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    publish = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='blog_posts', null=True)
    content = models.TextField()
    status = models.CharField(max_length=10, choices=options, default='draft')
    favourites = models.ManyToManyField(User, related_name='favourite', default=None, blank=True)
    likes = models.ManyToManyField(User, related_name='like', default=None, blank=True)
    like_count = models.BigIntegerField(default='0')
    objects = models.Manager()  # default manager
    newmanager = NewManager()  # custom manager

    def get_absolute_url(self):
        return reverse('blog:post_single', args=[self.slug])

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.name


class Comment(MPTTModel):

    motorcycle = models.ForeignKey(Motorcycles, on_delete=models.CASCADE, related_name='comments',null=True)
    name = models.CharField(max_length=50)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    email = models.EmailField()
    content = models.TextField()
    publish = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class MPTTMeta:
        order_insertion_by = ['publish']

    def __str__(self):
        return self.name

class PanosCustoms(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    address = models.CharField(max_length=80)
    city = models.CharField(max_length=30, null=True)
    phone = PhoneNumberField(unique=True)

    def __str__(self):
        return f"{self.name} Email: {self.email} Phone: {self.phone} Address: {self.address}, {self.city} " 