from django.contrib import admin
from .models import ChaiVariety, ChaiReviews


class ChaiReviewsAdmin(admin.TabularInline) :
    model = ChaiReviews
    extra = 1
class ChaiVarietyAdmin(admin.ModelAdmin) :
    list_display = ('name', 'image', 'date_added', 'type', 'description')
    inlines = [ChaiReviewsAdmin]

# Register your models here.
admin.site.register(ChaiVariety, ChaiVarietyAdmin)