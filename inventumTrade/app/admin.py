from django.contrib import admin
from .models import *


class ResearchAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "text", "image")
    prepopulated_fields = {"slug": ("title",)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", )
    prepopulated_fields = {"slug": ("title",)}


class VacancyAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "image")
    prepopulated_fields = {"slug": ("title",)}



admin.site.register(Research, ResearchAdmin)
admin.site.register(Vacancy, VacancyAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Profile)
admin.site.register(ReviewRating)