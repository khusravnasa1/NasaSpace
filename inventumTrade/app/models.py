from django.db import models
from django.contrib.auth.models import User
import datetime
import os
from django.urls import reverse
from django.template.defaultfilters import slugify


def get_file_path(request, filename):
    original_filename = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (nowTime, original_filename)
    return os.path.join('uploads/', filename)


class Category(models.Model):
    title = models.CharField(max_length=150, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=True, unique=True)  # new

    def __str__(self):
        return self.title



    def get_absolute_url(self):
        return reverse("login", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title + self.author)
        return super().save(*args, **kwargs)


class Research(models.Model):
    categories = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name='categories')
    teg1 = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False, null=True, related_name='teg1')
    teg2 = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name='teg2')
    teg3 = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name='teg3')
    teg4 = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name='teg4')
    teg5 = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name='teg5')

    title = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to=get_file_path, null=False, blank=False)
    description = models.CharField(max_length=300, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(null=False, blank=False)
    slug = models.SlugField(null=True, unique=True)  # new
    need1 = models.CharField(max_length=120, null=False, blank=True)
    need2 = models.CharField(max_length=120, null=False, blank=True)
    need3 = models.CharField(max_length=120, null=False, blank=True)
    need4 = models.CharField(max_length=120, null=False, blank=True)
    need5 = models.CharField(max_length=120, null=False, blank=True)
    need6 = models.CharField(max_length=120, null=False, blank=True)
    need7 = models.CharField(max_length=120, null=False, blank=True)
    need8 = models.CharField(max_length=120, null=False, blank=True)
    need9 = models.CharField(max_length=120, null=False, blank=True)
    need10 = models.CharField(max_length=120, null=False, blank=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Vacancy(models.Model):
    title = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to=get_file_path, null=False, blank=False)
    description = models.CharField(max_length=300, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    slug = models.SlugField(null=True, unique=True)  # new

    def __str__(self):
        return self.title



    def get_absolute_url(self):
        return reverse("login", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title + self.author)
        return super().save(*args, **kwargs)


class Profile(models.Model):
    title = models.CharField(max_length=150, null=True, blank=False)
    file = models.FileField(null=True, upload_to=get_file_path)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    cover_letter = models.TextField(null=True, blank=True)


class ReviewRating(models.Model):
    research = models.ForeignKey(Research, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100, blank=True)
    review = models.TextField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject

