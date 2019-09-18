from django.contrib import admin
from api.models import Account, Review


@admin.register(Account)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'rating', 'title', 'company')